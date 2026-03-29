select
    country_slug,
    country,
    observation_year,
    observation_month,
    count(*) as anomaly_count,
    avg(brightness) as avg_brightness,
    avg(frp) as avg_frp,
    max(frp) as max_frp
from {{ ref('stg_thermal_anomalies') }}
group by 1,2,3,4
