--- 1. Clean and Prepare Customer Journey Data ---
-- This query cleans the raw customer journey data by removing duplicate events and
-- filling in missing session durations, making it reliable for funnel analysis.

SELECT
	cj.journeyid,
	cj.customerid,
	cj.productid,
	cj.visitdate,
	cj.stage,
	upper(cj."Action") AS action,
	-- Impute missing duration values. If a session's duration is NULL,
	-- we fill it with the average duration calculated for that specific day.
	COALESCE(cj.duration, cj.avg_duration) AS duration
FROM (
	-- This inner query performs the heavy lifting: calculating daily averages and flagging duplicates.
	SELECT
		sub.journeyid,
		sub.productid,
		sub.customerid,
		sub."Action",
		sub.visitdate,
		sub.duration,
		sub.stage,
		-- Window function to calculate the average session duration for each visit date.
		-- This value is used above to fill in any nulls.
		avg(sub.duration) OVER (PARTITION BY sub.visitdate) AS avg_duration,
		-- Window function to identify duplicate records. It assigns a rank to each event
		-- based on a unique combination of fields, ordered by journeyid.
		ROW_NUMBER() OVER (
			PARTITION BY sub.customerid, sub.productid, sub.visitdate, sub.stage, sub."Action"
			ORDER BY sub.journeyid
		) AS row_num
	FROM
		customer_journey AS sub
) AS cj
WHERE
	cj.row_num = 1; -- The final step: filter out the duplicates, keeping only the first unique event.
