from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

# Initialize Spark session
spark = SparkSession.builder.appName("DataTransformation").getOrCreate()

# Define schema if necessary, matching the raw data structure
schema = StructType([
    StructField("deviceId", StringType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("timestamp", TimestampType(), True)
])

# Load raw data
raw_data_path = "/mnt/datalake/raw/ingested_data/"
raw_df = spark.read.format("delta").schema(schema).load(raw_data_path)

# Cleanse and transform data
transformed_df = raw_df \
    .filter(col("temperature").isNotNull()) \
    .withColumn("temperature_celsius", (col("temperature") - 32) * 5.0/9.0)  # Example conversion to Celsius

# Aggregations or further processing (if needed)
average_temp_df = transformed_df \
    .groupBy("deviceId") \
    .agg(avg("temperature_celsius").alias("average_temperature"))

# Write transformed data to the processed layer
processed_data_path = "/mnt/datalake/processed/transformed_data/"
query = average_temp_df \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/datalake/checkpoints/transformation_checkpoint") \
    .start(processed_data_path)

query.awaitTermination()
