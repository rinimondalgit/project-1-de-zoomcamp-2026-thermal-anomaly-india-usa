import os
from google.cloud import bigquery, storage

def upload_curated_to_gcs(bucket_name, local_path):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    for root, dirs, files in os.walk(local_path):
        for file in files:
            if file.endswith(".parquet"):
                local_file = os.path.join(root, file)

                # Preserve partition folder structure
                relative_path = os.path.relpath(local_file, local_path)
                gcs_path = f"thermal_anomaly/curated/{relative_path}"

                blob = bucket.blob(gcs_path)
                blob.upload_from_filename(local_file)

                print(f"Uploaded {local_file} → gs://{bucket_name}/{gcs_path}")


def main():
    project_id = os.environ["GCP_PROJECT_ID"]
    dataset_id = os.environ["BQ_DATASET"]
    bucket = os.environ["GCS_BUCKET"]

    local_curated_path = "/opt/airflow/data/outputs/curated"

    # ✅ Step 1: Upload parquet to GCS
    upload_curated_to_gcs(bucket, local_curated_path)

    # ✅ Step 2: Create external table
    client = bigquery.Client(project=project_id)
    dataset_ref = f"{project_id}.{dataset_id}"

    external_table_id = f"{dataset_ref}.ext_thermal_anomaly_curated"
    curated_table_id = f"{dataset_ref}.thermal_anomaly_curated"

    external_config = bigquery.ExternalConfig("PARQUET")
    external_config.source_uris = [f"gs://{bucket}/thermal_anomaly/curated/*"]

    external_table = bigquery.Table(external_table_id)
    external_table.external_data_configuration = external_config

    client.delete_table(external_table_id, not_found_ok=True)
    client.create_table(external_table)

    # ✅ Step 3: Create final table
    sql = f"""
    CREATE OR REPLACE TABLE `{curated_table_id}` AS
    SELECT *
    FROM `{external_table_id}`
    """
    client.query(sql).result()

    print(f"Created curated table: {curated_table_id}")


if __name__ == "__main__":
    main()