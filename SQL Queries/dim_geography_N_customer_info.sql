--- Create Customer Demographics View ---
-- This query joins customer and geography data and creates a new 'age_group'
-- column for easier demographic segmentation.
SELECT
	c.customerid,
	c.customername,
	c.age,
	-- Segment customers into descriptive age groups based on their age.
	CASE
		WHEN c.age >= 55 THEN 'Senior(55+)'
		WHEN c.age BETWEEN 40 AND 54 THEN 'Middle-aged(40-54)'
		WHEN c.age BETWEEN 25 AND 39 THEN 'Adult(25-39)'
		ELSE 'Young Adult(<25)'
	END AS age_group,
	c.email,
	c.gender,
	g.city,
	g.country
FROM
	customers c
LEFT JOIN geography g ON
	c.geographyid = g.geographyid;
