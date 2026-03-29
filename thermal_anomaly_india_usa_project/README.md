📊 Thermal Anomaly Data Pipeline (India 🇮🇳 vs USA 🇺🇸)





🚀 Project Overview

Thermal anomalies—such as wildfires, volcanic activity, and other heat sources—have become increasingly significant due to climate change, environmental shifts, and human impact. Recent large-scale events have highlighted the need for better monitoring, analysis, and understanding of these phenomena.



This project provides a data-driven analytical framework to explore global thermal anomalies using satellite-derived datasets. By leveraging observations from NASA’s MODIS (Moderate Resolution Imaging Spectroradiometer), the project systematically processes and analyzes thermal activity across different regions and time periods.



This project builds an end-to-end data engineering pipeline to process and analyze thermal anomaly (fire) data from NASA FIRMS for India and the United States (2019–2024).



The pipeline ingests raw CSV data, processes it using PySpark, and loads curated datasets into BigQuery for analytics.
![Architecture](image/image.png)
🎯 Objective



The primary goal of this project is to:



Aggregate and process global thermal anomaly data

Classify anomaly events into meaningful categories

Analyze spatial and temporal trends

Generate insights into regional risk patterns and anomaly behavior



The analysis enables identification of:



Regions with increasing wildfire or thermal activity

Distribution patterns across anomaly types

Long-term trends in intensity and frequency

📊 Data Source



The project utilizes MODIS satellite data, which captures thermal anomalies across the Earth’s surface. These datasets provide:



Global coverage

High temporal frequency

Consistent measurement of thermal signals



The data includes attributes such as:



Geographic coordinates

Brightness temperature

Detection confidence

Timestamp and satellite metadata

🧩 Classification of Thermal Anomalies



Detected thermal events are categorized into four primary classes:



Vegetation Fires – Wildfires and biomass burning events

Volcanic Activity – Thermal signals associated with volcanic regions

Static Land Sources – Industrial heat sources or persistent land-based anomalies

Offshore Sources – Marine-based thermal detections such as gas flaring



This classification enables more granular analysis of anomaly types and their distribution.



🧱 Architecture

&#x20;               ┌────────────────────────┐

&#x20;               │  NASA FIRMS CSV Data   │

&#x20;               │  (India + USA)         │

&#x20;               └──────────┬─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;               ┌────────────────────────┐

&#x20;               │ Local Raw Storage      │

&#x20;               │ /data/raw              │

&#x20;               └──────────┬─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;               ┌────────────────────────┐

&#x20;               │ Airflow DAG 1          │

&#x20;               │ extract\_raw\_to\_gcs     │

&#x20;               └──────────┬─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;               ┌────────────────────────┐

&#x20;               │ GCS Bucket (RAW)       │

&#x20;               │ thermal\_anomaly/raw    │

&#x20;               └──────────┬─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;               ┌────────────────────────┐

&#x20;               │ Airflow DAG 2          │

&#x20;               │ transform\_raw\_to\_curated│

&#x20;               │ (PySpark)              │

&#x20;               └──────────┬─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;               ┌────────────────────────┐

&#x20;               │ Local Curated Parquet  │

&#x20;               │ /data/outputs/curated  │

&#x20;               └──────────┬─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;               ┌────────────────────────┐

&#x20;               │ Airflow DAG 3          │

&#x20;               │ load\_curated\_to\_bq     │

&#x20;               └──────────┬─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;               ┌────────────────────────┐

&#x20;               │ GCS (Curated)          │

&#x20;               │ thermal\_anomaly/curated│

&#x20;               └──────────┬─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;               ┌────────────────────────┐

&#x20;               │ BigQuery               │

&#x20;               │ thermal\_anomaly\_dw     │

&#x20;               │ final analytics table  │

&#x20;               └────────────────────────┘

🛠️ Tech Stack

Cloud: Google Cloud Platform (GCP)

Storage: Google Cloud Storage (GCS)

Data Warehouse: BigQuery

Orchestration: Apache Airflow (Docker)

Processing: PySpark

Infrastructure as Code: Terraform

Language: Python

⚙️ Pipeline Components

1️⃣ Data Ingestion (Airflow DAG)

Uploads raw CSV files to GCS

Supports multiple countries and years

Handles file pattern parsing

2️⃣ Data Transformation (PySpark)

Reads raw CSV data

Extracts:

country (from filename)

year (from filename)

Cleans and standardizes data

Writes curated parquet files

3️⃣ Data Loading (BigQuery)

Uploads parquet files to GCS

Creates external table

Loads data into final BigQuery table

📂 Project Structure

thermal\_anomaly\_india\_usa\_project/

│

├── airflow/

│   ├── dags/

│   │   ├── extract\_raw\_to\_gcs\_dag.py

│   │   ├── transform\_raw\_to\_curated\_dag.py

│   │   └── load\_curated\_to\_bigquery\_dag.py

│   ├── scripts/

│   │   ├── extract\_and\_upload.py

│   │   ├── load\_to\_bigquery.py

│   │   └── helpers.py

│   ├── Dockerfile

│   └── requirements.txt

│

├── spark/

│   └── transform\_to\_parquet.py

│

├── terraform/

│   ├── main.tf

│   └── variables.tf

│

├── data/

│   ├── raw/

│   └── outputs/

│

├── .env

└── README.md

▶️ How to Run

1\. Setup GCP

Create project

Enable billing

Create service account

Assign roles:

Storage Admin

BigQuery Admin

2\. Provision Infrastructure

cd terraform

terraform init

terraform apply

3\. Start Airflow

cd airflow

docker-compose up airflow-init

docker-compose up -d

4\. Run DAGs (in order)

extract\_raw\_to\_gcs

transform\_raw\_to\_curated

load\_curated\_to\_bigquery

📊 Example Query

SELECT country, year, COUNT(\*) AS records

FROM `de-zoomcamp-thermal-anomaly-12.thermal\_anomaly\_dw.thermal\_anomaly\_curated`

GROUP BY country, year

ORDER BY year, country;

📸 Screenshots 

Airflow DAGs (all green)

GCS raw + curated folders

BigQuery dataset and table

query result



Dashboard Visualization - Google lookers studio



Open Data Studio : https://lookerstudio.google.com/.



Data Source: Select BigQuery. Find table  in the project/dataset. Click CONNECT.



Create Report. Add to the report.

Create a dashboard by adding charts as follows:
https://github.com/rinimondalgit/project-1-de-zoomcamp-2026-thermal-anomaly-india-usa/blob/main/thermal_anomaly_india_usa_project/images/executive.png
https://github.com/rinimondalgit/project-1-de-zoomcamp-2026-thermal-anomaly-india-usa/blob/main/thermal_anomaly_india_usa_project/images/India.png
https://github.com/rinimondalgit/project-1-de-zoomcamp-2026-thermal-anomaly-india-usa/blob/main/thermal_anomaly_india_usa_project/images/usa.png
https://github.com/rinimondalgit/project-1-de-zoomcamp-2026-thermal-anomaly-india-usa/blob/main/thermal_anomaly_india_usa_project/images/comparison.png
https://github.com/rinimondalgit/project-1-de-zoomcamp-2026-thermal-anomaly-india-usa/blob/main/thermal_anomaly_india_usa_project/images/spatial.png
https://github.com/rinimondalgit/project-1-de-zoomcamp-2026-thermal-anomaly-india-usa/blob/main/thermal_anomaly_india_usa_project/images/insight.png





🚧 Challenges \& Solutions

❌ Spark couldn’t read gs://



✔️ Fixed by using local mounted paths and uploading curated data separately



❌ Missing pyspark



✔️ Fixed by updating Docker requirements and rebuilding image



❌ Filename parsing issues



✔️ Built regex-based parser for country/year extraction



❌ IAM permission errors



✔️ Added required roles to service account



❌ BigQuery couldn’t find files



✔️ Uploaded curated parquet to GCS before loading



💡 Key Learnings

End-to-end pipeline orchestration using Airflow

Handling real-world dependency conflicts in Docker

Spark + GCS integration challenges

Designing hybrid local + cloud data pipelines

Managing IAM and GCP services



📌 Conclusion



This project demonstrates how large-scale satellite data can be transformed into actionable insights through structured data engineering and analysis. By combining classification, aggregation, and visualization, it provides a comprehensive view of global thermal anomaly patterns and their evolution over time.

