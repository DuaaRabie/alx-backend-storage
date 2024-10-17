-- task2
-- Best band ever!

WITH ranked_countries AS (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY nb_fans DESC) AS rank,
        origin,
        nb_fans
    FROM 
        metal_bands
)
SELECT *
FROM ranked_countries
ORDER BY 
    nb_fans DESC;
