-- task2
-- Best band ever!

WITH ranked_countries AS (
    SELECT origin, COUNT(*) AS nb_fans
    FROM metal_bands
    GROUP BY origin
)
SELECT origin, nb_fans,
       RANK() OVER (ORDER BY nb_fans DESC) AS rank
FROM ranked_countries
ORDER BY nb_fans DESC;

