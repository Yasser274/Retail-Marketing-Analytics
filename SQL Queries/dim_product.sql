--- Create Product Price Tiers ---
-- Segments products into price categories for high-level analysis.
SELECT
	p.productid,
	p.productname,
	p.price,
	-- Categorize products into 'Low', 'Medium', or 'High' price tiers.
	CASE
		WHEN p.price < 50 THEN 'Low'
		WHEN p.price BETWEEN 50 AND 200 THEN 'Medium'
		ELSE 'High'
	END AS price_category
FROM
	products p;
