"""
This script performs an end-to-end sentiment analysis on customer review data.
It connects to a PostgreSQL database, fetches review and customer information,
engineers new features like sentiment scores and age groups, and exports the
enriched data to a CSV file for further analysis in tools like Power BI.
"""

# --- 1. SETUP & CONFIGURATION ---

# Load environment variables from the .env file for secure database credentials
load_dotenv()

# --- 2. NLTK VADER LEXICON MANAGEMENT ---
# To make this project portable, I'll manage the NLTK data locally.
# This ensures that anyone running the script has the necessary VADER lexicon
# without needing to install it system-wide.

# Define a local directory for NLTK data within the project folder.
local_nltk_data_dir = os.path.join(os.path.dirname(__file__), "nltk_data")

# Create the directory if it doesn't already exist.
if not os.path.exists(local_nltk_data_dir):
    os.makedirs(local_nltk_data_dir)

# Download the VADER lexicon only if it's not found in our local directory.
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
    print("VADER lexicon is already available locally.")
except LookupError:
    print(f"Downloading VADER lexicon to '{local_nltk_data_dir}'...")
    nltk.download("vader_lexicon", download_dir=local_nltk_data_dir)
    print("Download complete.")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# --- 3. DATA FETCHING ---
def fetch_data_sql():
    """
    Connects to the PostgreSQL database using credentials from the .env file,
    executes a query to join customer and review data, and returns the result
    as a pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the queried data, or None if the
                      connection fails.
    """

    # Retrieve database configuration from environment variables.
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")

    # Ensure all required environment variables are set.
    if not all([db_host, db_port, db_pass, db_user, db_name]):
        print("Error: One or more database environment variables are not set.")
        return None
    conn = None
  
    try:
        # Establish the database connection.
        conn = psycopg2.connect(
            host=db_host, port=db_port, database=db_name, user=db_user, password=db_pass
        )
        print("Connected to PostgreSQL database successfully.")

        # SQL query to fetch and join the necessary tables.
        query = """
            SELECT
                c.customerid, c.age,
                cr.reviewdate::date AS review_date, cr.rating, cr.reviewtext,
                p.productid
            FROM customer_reviews cr
            LEFT JOIN customers c ON c.customerid = cr.customerid
            LEFT JOIN products p ON p.productid = cr.productid
        """
      
      # Use pandas to execute the query and load data directly into a DataFrame.
        df = pd.read_sql_query(query, conn)
        print(f"Successfully fetched {len(df)} rows into a DataFrame.")
        return df
      
      except psycopg2.OperationalError as e:
        print(f"Could not connect to the database: {e}")
        return None
    finally:
        # Always close the connection, whether the query succeeded or failed.
        if conn:
            conn.close()
            print("Database connection closed.")


# --- 4. SENTIMENT ANALYSIS & FEATURE ENGINEERING ---

# Initialize the VADER sentiment intensity analyzer.
sia = SentimentIntensityAnalyzer()

def calculate_sentiment(review_text):
    """Calculates the compound sentiment score for a given text using VADER."""
    # The 'compound' score is a single metric that summarizes the sentiment.
    return sia.polarity_scores(review_text)["compound"]

def categorize_sentiment(score, rating):
    """
    Creates nuanced sentiment categories by combining the text's sentiment score
    with the user's star rating. This provides a more accurate picture than
    relying on the text or rating alone.

    For example, positive text with a low rating is categorized as "Mixed Negative."
    """
    if score > 0.05:  # Positive text sentiment
        if rating >= 4:
            return "Positive"
        elif rating == 3:
            return "Mixed Positive"
        else:  # Rating is 1 or 2
            return "Mixed Negative"
    elif score < -0.05:  # Negative text sentiment
        if rating <= 2:
            return "Negative"
        elif rating == 3:
            return "Mixed Negative"
        else:  # Rating is 4 or 5
            return "Mixed Positive"
    else:  # Neutral text sentiment
        if rating >= 4:
            return "Positive"
        elif rating <= 2:
            return "Negative"
        else:  # Rating is 3
            return "Neutral"

def sentiment_bucketF(score):
    """Categorizes a sentiment score into one of four descriptive buckets."""
    if score >= 0.05:
        return "Positive (0.05 to 1.0)"
    elif 0.0 <= score < 0.05:
        return "Neutral (0.0 to 0.05)"
    elif -0.5 <= score < 0.0:
        return "Mildly Negative (-0.5 to 0.0)"
    else:
        return "Strongly Negative (-1.0 to -0.5)"

# --- 5. DATA PROCESSING & EXPORT ---
# Fetch the initial dataset.
customer_reviews = fetch_data_sql()
# Apply the feature engineering functions to create new columns. (Just to make sure the code is running until this point)
print("Starting feature engineering...")

# Calculate the sentiment score for each review using the efficient .apply() method.
customer_reviews["sentiment_score"] = customer_reviews["reviewtext"].apply(calculate_sentiment)

# Create the nuanced sentiment category by applying my custom logic to each row.
# I use a lambda function with axis=1 to pass both 'sentiment_score' and 'rating'
# from each row into our function.
customer_reviews["sentiment_category"] = customer_reviews.apply(
    lambda row: categorize_sentiment(row["sentiment_score"], row["rating"]), axis=1
)

# Create sentiment score buckets.
customer_reviews["sentiment_bucket"] = customer_reviews["sentiment_score"].apply(sentiment_bucketF)

# Define bins and labels for segmenting customers into age groups.
age_bins = [0, 24, 39, 54, 120]
age_labels = ["Young Adult (<25)", "Adult (25-39)", "Middle-Aged (40-54)", "Senior (55+)"]

# Use pandas.cut to bin customers into their respective age groups.
customer_reviews["age_group"] = pd.cut(
    customer_reviews["age"], bins=age_bins, labels=age_labels, right=True
)

# A final cleaning step to normalize whitespace in the review text.
customer_reviews["reviewtext"] = customer_reviews["reviewtext"].str.replace(r'\s+', ' ', regex=True).str.strip()

# Display the first few rows of the enriched DataFrame to verify the results.
print("Feature engineering complete. Enriched DataFrame head:")
print(customer_reviews.head())

# Export the final, cleaned DataFrame to a CSV file.
output_filename = "fact_customer_reviews_sentiments.csv"
customer_reviews.to_csv(output_filename, index=False)
print(f"Successfully exported data to {output_filename}")
