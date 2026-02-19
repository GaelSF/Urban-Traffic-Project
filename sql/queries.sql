-- 1. Velocidad promedio global
SELECT AVG(avg_velocity) AS overall_avg_speed
FROM traffic_metrics;

-- 2. Tiempo con mayor congestión
SELECT time, congestion_index
FROM traffic_metrics
ORDER BY congestion_index DESC
LIMIT 5;

-- 3. Conteo por nivel de tráfico
SELECT traffic_level, COUNT(*) as count
FROM traffic_metrics
GROUP BY traffic_level;

-- 4. Evolución de congestión
SELECT time, congestion_index
FROM traffic_metrics
ORDER BY time;
