import os
import re
from pathlib import Path

VALID_COUNTRIES = {"india", "united_states", "unitedstates", "usa", "us"}

def slugify_country(country: str) -> str:
    country = country.strip().lower().replace(" ", "_")
    aliases = {
        "usa": "united_states",
        "us": "united_states",
        "unitedstates": "united_states",
    }
    return aliases.get(country, country)



def infer_country_year(filename: str):
    patterns = [
        r"modis_(\d{4})_(India|United_States)\.csv",
        r"MODIS_C6_1_(India|United_States)_(\d{4})\.csv",
        r"MODIS_C6_1_(India|United States)_(\d{4})\.csv",
    ]

    for pattern in patterns:
        match = re.match(pattern, filename, re.IGNORECASE)
        if match:
            g1, g2 = match.groups()

            # Handle either (year, country) or (country, year)
            if g1.isdigit():
                year = g1
                country = g2
            else:
                country = g1
                year = g2

            country = country.replace("_", " ")
            return country, int(year)

    raise ValueError(f"Could not infer country/year from filename: {filename}")

def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Missing required env var: {name}")
    return value
