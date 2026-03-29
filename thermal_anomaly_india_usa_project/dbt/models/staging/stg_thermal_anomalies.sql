select
    cast(latitude as float64) as latitude,
    cast(longitude as float64) as longitude,
    cast(brightness as float64) as brightness,
    cast(scan as float64) as scan,
    cast(track as float64) as track,
    date(observation_date) as observation_date,
    cast(observation_year as int64) as observation_year,
    cast(observation_month as int64) as observation_month,
    cast(frp as float64) as frp,
    cast(bright_t31 as float64) as bright_t31,
    cast(country as string) as country,
    cast(country_slug as string) as country_slug,
    cast(confidence_band as string) as confidence_band,
    cast(frp_band as string) as frp_band,
    cast(daynight as string) as daynight,
    cast(satellite as string) as satellite,
    cast(version as string) as version
from `{{ env_var("GCP_PROJECT_ID") }}.{{ env_var("BQ_DATASET") }}.thermal_anomaly_curated`
