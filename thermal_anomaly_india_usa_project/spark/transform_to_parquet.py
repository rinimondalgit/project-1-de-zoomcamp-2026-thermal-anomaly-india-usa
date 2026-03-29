from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    input_file_name,
    regexp_extract,
    col,
    to_date,
    lit,
)
from pyspark.sql.types import IntegerType
import os


def main():
    spark = (
        SparkSession.builder
        .appName("thermal-anomaly-transform")
        .getOrCreate()
    )

    raw_path = "/opt/airflow/data/raw/*.csv"
    curated_path = "/opt/airflow/data/outputs/curated"

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(raw_path)
    )

    # Add source filename
    df = df.withColumn("source_file", input_file_name())

    # Extract year and country from filenames like:
    # modis_2019_India.csv
    # modis_2020_United_States.csv
    df = df.withColumn(
        "year",
        regexp_extract(col("source_file"), r"modis_(\d{4})_", 1).cast(IntegerType())
    )

    df = df.withColumn(
        "country",
        regexp_extract(col("source_file"), r"modis_\d{4}_(.+)\.csv", 1)
    )

    # Normalize country names
    df = df.withColumn(
        "country",
        regexp_extract(col("country"), r"(.*)", 1)
    ).replace("United_States", "United States", subset=["country"])

    # Parse date if present
    if "acq_date" in df.columns:
        df = df.withColumn("acq_date", to_date(col("acq_date")))

    # Add month if acq_date exists
    if "acq_date" in df.columns:
        from pyspark.sql.functions import month
        df = df.withColumn("month", month(col("acq_date")))

    # Optional sanity check
    required_cols = ["country", "year"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns after transformation: {missing}")

    # Clean output folder behavior
    (
        df.write
        .mode("overwrite")
        .parquet(curated_path)
    )

    print(f"Curated parquet written to: {curated_path}")
    spark.stop()


if __name__ == "__main__":
    main()