# Databricks notebook source
import os
import requests
import json
import datetime


class FeeddexAPI:
    def __init__(self, root_url, organization):
        # Initialize the API with the root URL and organization name
        self.root_url = root_url
        self.organization = organization
        self.DATABRICKS_SECRET_SCOPE_ATM = "<ENTER DATABRICKS SCOPE"
        # Retrieve username and password from Databricks secret scope
        self.username = dbutils.secrets.get(
            scope=self.DATABRICKS_SECRET_SCOPE_ATM, key="<ENTER USERNAME AS PROVIDED BY FEEDDEX>")
        self.password = dbutils.secrets.get(
            scope=self.DATABRICKS_SECRET_SCOPE_ATM, key="<ENTER PASSWORD AS PROVIDED BY FEEDDEX>")
        self.version = "v1"
        # Authenticate and get the token
        self.token = self._authenticate()

    def _authenticate(self):
        # Prepare authentication data
        auth_data = {
            "authCode": self.username,
            "organization": self.organization,
            "password": self.password
        }
        # Send POST request to authenticate and get the token
        response = requests.post(
            os.path.join(self.root_url, "authenticate"),
            json=auth_data
        )
        response.raise_for_status()  # Raise an exception for error HTTP status codes
        return response.json()["token"]

    def get_feedback_data(self, year=datetime.datetime.now().strftime("%Y"), month=datetime.datetime.now().strftime("%m")):
        # Set up headers with the authorization token
        headers = {"Authorization": f"Bearer {self.token}"}
        # Set up parameters for the request
        params = {"year": year, "month": month}
        # Send GET request to retrieve feedback data
        r_data = requests.get(
            os.path.join(self.root_url, self.version, "feedbackData"),
            headers=headers,
            params=params
        )
        r_data.raise_for_status()  # Raise an exception for error HTTP status codes
        return r_data


# Define the root URL and organization
root_url = "https://api.feeddex.nl"
organization = "<ENTER ORGANIZATION NAME AS PROVIDED BY FEEDDEX>"
# Create an instance of the FeeddexAPI class
feeddex_api = FeeddexAPI(root_url, organization)
# Get feedback data
r_data = feeddex_api.get_feedback_data()
# Get the content of the response
content = r_data.content
# Parse the JSON content
d = json.loads(r_data.content)


# COMMAND ----------

from pyspark.sql.types import StringType, DateType, IntegerType, TimestampType, StructType, StructField, FloatType
from datetime import datetime
from pyspark.sql import functions as F
from pyspark.sql.functions import col, round


class FeedbackDataProcessor:
    def __init__(self, spark):
        # Initialize the FeedbackDataProcessor with a Spark session
        self.spark = spark

        # Define the schema for the feedback data
        self.feedback_schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("date", DateType(), True),
            StructField("customerCode", IntegerType(), True),
            StructField("unitId", IntegerType(), True),
            StructField("enteredOn", TimestampType(), True),
            StructField("sentOn", TimestampType(), True),
            StructField("remindedOn", TimestampType(), True),
            StructField("feedbackStarted", TimestampType(), True),
            StructField("modelQuestionsCompleted", TimestampType(), True),
            StructField("feedbackCompleted", TimestampType(), True),
            StructField("expirationDate", DateType(), True),
            StructField("value", IntegerType(), True),
            StructField("valueAsGrade", FloatType(), True),
        ])

        # Define the schema for the unit data
        self.unit_schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("name", StringType(), True)
        ])

    def parse_date(self, date_str, date_format="%Y-%m-%d"):
        # Parse a date string into a date object
        return datetime.strptime(date_str, date_format).date() if date_str else None

    def parse_timestamp(self, timestamp_str, timestamp_format="%Y-%m-%dT%H:%M:%S.%fZ"):
        # Parse a timestamp string into a datetime object
        return datetime.strptime(timestamp_str, timestamp_format) if timestamp_str else None

    def process_feedback_data(self, feedback_data):
        # Process the feedback data and create a DataFrame
        data = [
            (
                int(f["transaction"]["id"]),
                self.parse_date(f["transaction"]["date"]),
                int(f["transaction"]["customerCode"]),
                int(f["transaction"]["unitId"]),
                self.parse_timestamp(f["transaction"]["enteredOn"]),
                self.parse_timestamp(f["transaction"]["sentOn"]),
                self.parse_timestamp(f["transaction"].get("remindedOn")),
                self.parse_timestamp(f["transaction"].get("feedbackStarted")),
                self.parse_timestamp(f["transaction"].get(
                    "modelQuestionsCompleted")),
                self.parse_timestamp(
                    f["transaction"].get("feedbackCompleted")),
                self.parse_date(f["transaction"].get("expirationDate")),
                f["f100Scores"]["overallScore"]["value"] if f["f100Scores"] else None,
                f["f100Scores"]["overallScore"]["valueAsGrade"] if f["f100Scores"] else None
            )
            for f in feedback_data
        ]
        return self.spark.createDataFrame(data, self.feedback_schema)

    def process_unit_data(self, unit_data):
        # Process the unit data and create a DataFrame
        return self.spark.createDataFrame(unit_data, self.unit_schema)

    def join_dataframes(self, feedback_df, unit_data_df):
        # Join the feedback and unit data DataFrames
        return feedback_df.join(unit_data_df, feedback_df["unitId"] == unit_data_df["id"], "left") \
            .select(
                feedback_df["id"].alias("transactionId"),
                "date",
                "customerCode",
                "unitId",
                unit_data_df["name"].alias("region"),
                "enteredOn",
                "sentOn",
                "remindedOn",
                "feedbackStarted",
                "modelQuestionsCompleted",
                "feedbackCompleted",
                "expirationDate",
                "value",
                "valueAsGrade"
        )

    def calculate_summary(self, df):
        # Calculate summary statistics from the processed DataFrame
        return df.withColumn("year", F.substring(col("modelQuestionsCompleted").cast(StringType()), 1, 4)) \
                 .withColumn("month", F.substring(col("modelQuestionsCompleted").cast(StringType()), 6, 2)) \
                 .groupBy("unitId", "region", "year", "month") \
                 .agg(
                     round((F.sum(F.coalesce(col("value"), F.lit(0))) /
                           F.count(col("value"))), 2).alias("avgValue"),
                     round((F.sum(F.coalesce(col("valueAsGrade"), F.lit(0))) /
                           F.count(col("valueAsGrade"))), 2).alias("avgValueAsGrade"),
                     F.countDistinct(col("customerCode")).alias(
                         "customersThisPeriod"),
                     F.sum(F.when(col("valueAsGrade") > 8, 1).otherwise(
                         0)).alias("promotors"),
                     F.sum(F.when((col("valueAsGrade") >= 0) & (
                         col("valueAsGrade") <= 6), 1).otherwise(0)).alias("detractors"),
                     F.sum(F.when((col("valueAsGrade") > 6) & (
                         col("valueAsGrade") <= 8), 1).otherwise(0)).alias("passives")
        ) \
            .withColumn("questionnairesCompleted", col("promotors") + col("passives") + col("detractors")) \
            .withColumn("netPromotorScore", 100 * round((col("promotors") / col("questionnairesCompleted")) - (col("detractors") / col("questionnairesCompleted")), 2)) \
            .orderBy("unitId", "year", "month")

    def process_data(self, feedback_data, unit_data):
        # Process the feedback and unit data, join them, and calculate summary statistics
        feedback_df = self.process_feedback_data(feedback_data)
        unit_data_df = self.process_unit_data(unit_data)
        processed_df = self.join_dataframes(feedback_df, unit_data_df)
        summary_df = self.calculate_summary(processed_df)
        return processed_df, summary_df


# Assuming you have a SparkSession named "spark"
processor = FeedbackDataProcessor(spark)
processed_df, summary_df = processor.process_data(
    d["feedbackData"], d["unitData"])


# COMMAND ----------

display(processed_df)
display(summary_df)

# COMMAND ----------

# MAGIC %environment
# MAGIC "client": "1"
# MAGIC "base_environment": ""
