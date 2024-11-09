from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# Initialize Spark session
spark = SparkSession.builder.appName("EventHubIngestion").getOrCreate()

# Event Hub configuration
connection_string = "YOUR_EVENT_HUB_CONNECTION_STRING"
event_hub_conf = {
    'eventhubs.connectionString': connection_string
}

# Define schema for incoming JSON data (example schema)
schema = StructType([
    StructField("deviceId", StringType(), True),
    StructField("temperature", StringType(), True),
    StructField("timestamp", TimestampType(), True)
])

# Read from Event Hub stream
raw_df = spark \
    .readStream \
    .format("eventhubs") \
    .options(**event_hub_conf) \
    .load()

# Decode data from binary and parse JSON
parsed_df = raw_df \
    .select(from_json(col("body").cast("string"), schema).alias("data")) \
    .select("data.*")

# Write output to temporary storage (for the transformation stage to consume)
output_path = "/mnt/datalake/raw/ingested_data/"
query = parsed_df \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/datalake/checkpoints/ingestion_checkpoint") \
    .start(output_path)

query.awaitTermination()
