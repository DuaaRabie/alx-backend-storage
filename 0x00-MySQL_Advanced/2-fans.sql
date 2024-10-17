-- task2
-- Best band ever!

SELECT 
    ROW_NUMBER() OVER (ORDER BY nb_fans DESC) AS rank,
    origin,
    nb_fans
FROM 
    metal_bands
ORDER BY 
    nb_fans DESC;
