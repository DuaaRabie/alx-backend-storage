-- task2
-- Best band ever

SELECT 
    origin,
    COUNT(*) AS nb_fans
FROM 
    metal_bands
GROUP BY 
    origin
ORDER BY 
    nb_fans DESC;
