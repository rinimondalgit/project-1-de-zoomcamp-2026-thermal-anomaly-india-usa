resource "google_storage_bucket" "thermal_bucket" {
  name                        = var.bucket_name
  location                    = var.location
  force_destroy               = false
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}

resource "google_bigquery_dataset" "thermal_dataset" {
  dataset_id = var.dataset_name
  location   = var.location
}
