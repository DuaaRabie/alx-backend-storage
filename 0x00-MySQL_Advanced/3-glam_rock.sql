-- task3
-- Old school band

SELECT
	band_name,
	DATEDIFF(formed, COALESCE(split, '2022')) as lifespan
FROM
	metal_bands
WHERE
	style = 'Glam rock'
ORDER BY
	lifespan DESC;
