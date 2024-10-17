-- task2
-- Best band ever!

SELECT origin, nb_fans
FROM (
    SELECT origin, nb_fans,
           DENSE_RANK() OVER (ORDER BY nb_fans DESC) AS rank
    FROM metal_bands
) ranked
WHERE rank <= 10
ORDER BY rank;
