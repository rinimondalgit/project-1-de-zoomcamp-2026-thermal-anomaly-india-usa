import os
from pathlib import Path
from google.cloud import storage
from helpers import infer_country_year, required_env

def upload_raw_files():
    bucket_name = required_env("GCS_BUCKET")
    raw_input_dir = Path(required_env("RAW_INPUT_DIR"))
    if not raw_input_dir.exists():
        raise FileNotFoundError(f"RAW_INPUT_DIR does not exist: {raw_input_dir}")

    client = storage.Client()
    bucket = client.bucket(bucket_name)

    uploaded = []
    for file_path in sorted(raw_input_dir.glob("*.csv")):
        country, year = infer_country_year(file_path.name)
        blob_path = f"thermal_anomaly/raw/country={country}/year={year}/{file_path.name}"
        blob = bucket.blob(blob_path)
        blob.upload_from_filename(str(file_path))
        uploaded.append(blob_path)

    if not uploaded:
        raise FileNotFoundError(f"No CSV files found in {raw_input_dir}")

    print("Uploaded files:")
    for item in uploaded:
        print(item)

if __name__ == "__main__":
    upload_raw_files()
