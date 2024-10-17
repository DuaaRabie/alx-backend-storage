-- task2
-- Best band ever!

SELECT origin, nb_fans
FROM (
    SELECT origin, COUNT(*) AS nb_fans
    FROM metal_bands
    GROUP BY origin
) ranked_countries
ORDER BY nb_fans DESC;
