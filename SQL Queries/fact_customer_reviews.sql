--- Clean Customer Reviews Data ---
-- A simple cleaning step for review text to ensure consistent formatting.
SELECT
	cr.customerid,
	cr.productid,
	cr.reviewdate::date AS review_date,
	cr.rating,
	-- Normalize whitespace by replacing any double spaces with a single space.
	REPLACE(cr.reviewtext, '  ', ' ') AS formatted_reviewText
FROM
	customer_reviews cr;
