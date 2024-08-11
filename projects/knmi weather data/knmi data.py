# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, when, round, year, month, dayofmonth, count as spark_count
import requests
import zipfile
import os
from concurrent.futures import ThreadPoolExecutor

# Initialize Spark session
spark = SparkSession.builder.appName("DataFrameInit").getOrCreate()

# List of regions to process. Add more regions if desired
regions = [260, 344]


class DataFrameInit:
    def __init__(self, regions):
        # Load dataframes for the given regions
        self.dataframes = self.load_dataframes(regions)

    def download_and_extract(self, region):
        # URL to download the zip file for the given region
        url = f"https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/daggegevens/etmgeg_{region}.zip"
        local_zip_path = f"/tmp/etmgeg_{region}.zip"
        local_txt_path = f"/tmp/etmgeg_{region}.txt"

        try:
            # Download the zip file
            response = requests.get(url)
            response.raise_for_status()
            with open(local_zip_path, 'wb') as file:
                file.write(response.content)

            # Extract the text file from the zip file
            with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
                zip_ref.extractall("/tmp")

            return local_txt_path
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file for region {region}: {e}")
            return None

    def load_dataframes(self, regions):
        dataframes = {}

        # Use ThreadPoolExecutor to download and extract files in parallel
        with ThreadPoolExecutor() as executor:
            region_urls = list(executor.map(
                self.download_and_extract, regions))

        for region, region_url in zip(regions, region_urls):
            if not region_url:
                continue

            try:
                # Read the text file into a Spark dataframe, skipping the first 51 rows
                rdd = spark.sparkContext.textFile(
                    region_url).zipWithIndex().filter(lambda x: x[1] >= 51).keys()
                df = spark.read.csv(
                    rdd, header=True, sep=",", inferSchema=True)

                # Select necessary columns, create new columns, and perform calculation
                df = df.select(col("YYYYMMDD").alias("Date"),
                               col("   TG").alias("Degrees Celsius"))
                df = df.withColumn("Date", to_date(col("Date"), "yyyyMMdd"))
                df = df.withColumn("Degrees Celsius", col(
                    "Degrees Celsius").cast("float") / 10)
                df = df.na.drop(subset=["Degrees Celsius"])
                df = df.withColumn("Degree Days", self.temp_to_degreeday(df))

                # Round the Degrees Celsius and Degree Days columns to 2 decimal places
                df = df.withColumn("Degrees Celsius", round(
                    col("Degrees Celsius"), 2))
                df = df.withColumn("Degree Days", round(col("Degree Days"), 2))

                # Split Date into Year, Month, and Day columns
                df = df.withColumn("Year", year(col("Date")))
                df = df.withColumn("Month", month(col("Date")))
                df = df.withColumn("Day", dayofmonth(col("Date")))

                # Reorder columns
                df = df.select("Date", "Year", "Month", "Day",
                               "Degrees Celsius", "Degree Days")

                # Cache the DataFrame to avoid recomputation
                df.cache()

                dataframes[region] = df

                # Create directory if it doesn't exist
                output_dir = "extracted_files"
                os.makedirs(output_dir, exist_ok=True)
                # Define output filename with region number
                output_file = f"{output_dir}/etmgeg_{region}.csv"
                # Save dataframe to CSV, overwrite if file exists. Don't save the index row
                df.write.csv(output_file, header=True, mode="overwrite")

            except Exception as e:
                print(f"Error processing file for region {region}: {e}")

        return dataframes

    def temp_to_degreeday(self, df):
        ref_temp = 18
        calc = ref_temp - col("Degrees Celsius")
        degree_days = when(calc > 0, calc).otherwise(0)
        month = col("Date").substr(6, 2)

        # Calculate degree days based on the month
        return when(month.isin("04", "05", "06", "07", "08", "09"), degree_days * 0.8) \
            .when(month.isin("03", "10"), degree_days) \
            .otherwise(degree_days * 1.1)


# Initialize the DataFrameInit class with the list of regions
df_init = DataFrameInit(regions)

# Access and display the most recent 365 records for each region. Alter limit if desired
for region, df in df_init.dataframes.items():
    print(f"\nDataframe for region {region}")
    recent_df = df.orderBy(col("Date").desc()).limit(365)
    display(recent_df)

    # Create a new DataFrame with Year, Month, and Amount of Degree Days
    degree_days_df = df.filter(col("Degree Days") > 0) \
                       .groupBy("Year", "Month") \
                       .agg(spark_count("Degree Days").alias("Amount of Degree Days")) \
                       .orderBy(col("Year").desc(), col("Month").desc())

    print(f"\nAmount of Degree Days per month for region {region}")
    display(degree_days_df)


# COMMAND ----------

# MAGIC %environment
# MAGIC "client": "1"
# MAGIC "base_environment": ""
