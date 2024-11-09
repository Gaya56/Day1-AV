SELECT deviceId, AVG(temperature_celsius) AS avg_temp
FROM delta.`/mnt/datalake/processed/transformed_data/`
GROUP BY deviceId
ORDER BY avg_temp DESC
LIMIT 10;
