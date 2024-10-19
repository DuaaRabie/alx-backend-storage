-- task3
-- Old school band

SELECT
	band_name,
	IFNULL(
		DATEDIFF(2022, COALESCE(split, '2022')),
		DATEDIFF(2022, formed)
	) as lifespan
FROM
	metal_bands
WHERE
	style = 'Glam rock'
ORDER BY
	lifespan DESC;
