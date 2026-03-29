select distinct
    country_slug,
    country
from {{ ref('stg_thermal_anomalies') }}
