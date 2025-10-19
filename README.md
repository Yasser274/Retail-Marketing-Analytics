# Marketing Analytics Project
After learning Power BI, SQL, and Python, I decided to deepen my skills by analyzing a real-world dataset and tackling a practical marketing problem. The goal is to gain insights into customer behavior, campaign effectiveness, and overall customer experience for an online retail business.

## Sample Data
The dataset contains marketing and customer experience metrics/KPIs for an online retail business. The aim is to export, clean, and analyze this data to understand trends, performance gaps, and opportunities for improvement.

## Key Points
#### Marketing Campaigns

- Low ROI on marketing campaigns

- Decline in customer engagement and conversion rates

#### Customer Experience

- Drop in customer engagement and satisfaction

- Low overall conversion rate

#### Marketing & Customer Data Provided

- Customer reviews

- Social media comments

- Campaign performance metrics

#### Key KPIs

- Conversion rate

- Customer engagement rate

- Average order value (AOV)

- Customer feedback score

#### Data Sources & Tables

- Customer Journey Table – Tracks customer movements through the website to analyze the conversion funnel

- Engagement Data Table – Measures engagement with different types of content

- Customer Reviews Table – Analyzes feedback to identify common themes and sentiment

- Customers Table – Provides demographic information

- Geography Table – Provides geographic details about customers

- Products Table – Provides product information
## Database Setup

I chose PostgreSQL for this project, leveraging my experience with it from my previous Trend Bites full-stack web app. The original dataset was provided in a Microsoft SQL Server format, so I used DBeaver to efficiently migrate all tables into my PostgreSQL environment.

## Work Process

- Exported and cleaned the data

- Combined customer reviews with ratings to perform sentiment analysis

- Calculated key metrics like conversion rate, engagement rate, and AOV

- Built Power BI dashboards with bookmarks and pop-up filter panels (Filter by Gender, Sentiment Category, Product)

- Analyzed trends and identified areas for improvement

## Analysis
1. ### Overall Customer & KPI Summary

- **Customer Reviews**
    - Product ratings ranged from 3.52 (lowest) to 3.93 (highest)
    
    - Overall average rating: 3.69
    
    - Products with ratings below 3.5 need attention to improve customer satisfaction

- **Conversion Rate**

    - January: 17.31% (highest overall conversion)
    
    - October: 6.11% (lowest overall conversion)
    
    - December: 11.41% (recovery after the dip)

- **Customer Engagement**

    - Views peaked in January and dipped through mid-year, reaching the lowest in December
    
    - Likes and clicks are significantly lower than views, indicating a need for more engaging content
    
    - Click-through rate remains at 19.59%, suggesting moderate effectiveness

- **Customer Demographics**

    - Middle-aged (40-54): 1,522 (36.25%)
    
    - Seniors (55+): 1,375 (32.75%)
    
    - Adults (25-39): 1,066 (25.39%)
    
    - Young Adults (<25): 236 (5.62%)
    
    - Total Customers: 4,199
    
    - Gender: 1,878 M / 2,321 F

2. ### Conversion Analysis

- **General Trend**

    - September and December showed strong conversions after January’s peak, indicating seasonal and campaign effects.

- **Lowest Conversion Month**

    - October: 6.11%
    
    - Almost no product performed well, signaling a critical area for targeted marketing and optimization.

- **Highest Conversion Month**

    - January: 17.31%
    
    - Ski Boots achieved 100% conversion — everyone who viewed the product purchased it. Likely due to seasonal demand and highly targeted marketing.
    
3. ### Customer Engagement Analysis

- **Content Type Performance:**

    - Blog posts drove the most views overall (January: 349,970; April: 346,031)
    
    - Videos outperformed in February (367,949 views, highest overall)
    
    - Social media content is a close second overall

- **Interaction vs. Views:**

    - Clicks and likes are much lower than views, showing a need for more engaging content

- **Actionable Insight:**

    - Experiment with interactive content such as polls, quizzes, contests, and tutorial videos to increase engagement

4. ### Customer Reviews Analysis

- **Product Ratings**

    - Best Product: Climbing Rope – 3.91
    
    - Worst Product: Golf Clubs – 3.48

- **By Gender Highest/Lowest**

    - Males: Climbing Rope 4.25 / Golf Clubs 3.24
    
    - Females: Dumbbells 3.91 / Boxing Gloves 3.39

- **Review Distribution**

    - 5 stars: 409
    
    - 4 stars: 431
    
    - 3 stars (neutral): 290
    
    - 2 stars: 153
    
    - 1 star: 80

- **Sentiment Analysis**

    - Positive: 840
    
    - Negative: 226
    
    - Mixed negative: 196
    
    - Mixed positive: 86
    
    - Neutral: 15
    
    **Insight:**
    
    - Positive reviews dominate, but mixed-negative feedback highlights opportunities for improvement
    
    - Focus on improving products with lower ratings and addressing customer complaints

## Goals & Recommendations
1.   **Increase Conversion Rates**

      - **Goal:** Identify factors affecting conversion and optimize the funnel

      - **Action:** Focus marketing efforts on high-converting products like Ski Boots and Hockey Sticks

2.   **Enhance Customer Engagement**

      - **Goal:** Determine which content types drive engagement
      
      - **Action:** Experiment with interactive posts, polls, contests, and video tutorials to increase likes and clicks

3.   **Improve Customer Feedback Scores**

      - **Goal:** Understand recurring feedback themes and improve products/services
      
      - **Action:** Follow up with customers who left negative or mixed reviews to understand pain points and encourage updated ratings. Aim for an average rating of 4.0
