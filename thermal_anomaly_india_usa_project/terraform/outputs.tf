output "bucket_name" {
  value = google_storage_bucket.thermal_bucket.name
}

output "dataset_name" {
  value = google_bigquery_dataset.thermal_dataset.dataset_id
}
