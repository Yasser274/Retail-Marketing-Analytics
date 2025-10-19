--- Transform and Enrich Engagement Data ---
-- Prepares the engagement data by cleaning content types and splitting combined metrics.
SELECT
	ed.contentid,
	p.price,
	-- Standardize the 'contenttype' column for consistency (e.g., 'Socialmedia' -> 'Social Media').
	INITCAP(REGEXP_REPLACE(ed.contenttype, 'Socialmedia', 'Social media', 'gi')) AS formatted_content_type,
	ed.engagementdate,
	ed.campaignid,
	p.productid,
	ed.likes,
	-- Extract 'views' from the combined 'viewsclickscombined' string (e.g., '17-89' -> 17).
	split_part(ed.viewsclickscombined, '-', 1)::INTEGER AS views,
	-- Extract 'clicks' from the same combined string (e.g., '17-89' -> 89).
	split_part(ed.viewsclickscombined, '-', 2)::INTEGER AS clicks
FROM
	engagement_data ed
LEFT JOIN products p ON
	p.productid = ed.productid
WHERE
	ed.contenttype != 'Newsletter'; -- Exclude newsletter data as it's not relevant for this analysis.
