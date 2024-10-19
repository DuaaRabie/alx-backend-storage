-- task2
-- Best band ever

SELECT
	origin,
	fans AS nb_fans
FROM
	metal_bands
ORDER BY
	fans DESC;
