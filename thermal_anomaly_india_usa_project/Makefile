up:
	docker compose -f airflow/docker-compose.yml up --build

down:
	docker compose -f airflow/docker-compose.yml down

terraform-init:
	cd terraform && terraform init

terraform-plan:
	cd terraform && terraform plan

terraform-apply:
	cd terraform && terraform apply

dbt-run:
	cd dbt && dbt deps && dbt run && dbt test
