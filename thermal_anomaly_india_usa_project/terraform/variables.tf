variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "location" {
  description = "GCS / BigQuery location"
  type        = string
  default     = "US"
}

variable "bucket_name" {
  description = "Globally unique GCS bucket name"
  type        = string
}

variable "dataset_name" {
  description = "BigQuery dataset name"
  type        = string
  default     = "thermal_anomaly_dw"
}
