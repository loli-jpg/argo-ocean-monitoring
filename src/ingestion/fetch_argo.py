"""Загрузка данных Argo: статический CSV + динамический Argovis API."""
import requests
import pandas as pd
from pathlib import Path

ARGOVIS_URL = "https://argovis-api.colorado.edu/argo"


def fetch_profiles(start_date: str, end_date: str, polygon: str, data: str = "temperature"):
    """Запрос профилей к Argovis API с ограничением по времени и региону."""
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "polygon": polygon,
        "data": data,
    }
    response = requests.get(ARGOVIS_URL, params=params, timeout=60)
    if response.status_code == 413:
        raise ValueError("Запрос слишком большой — уменьшите регион или период.")
    response.raise_for_status()
    return response.json()


def save_raw(records, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(records).to_csv(path, index=False)


if __name__ == "__main__":
    records = fetch_profiles(
        start_date="2023-01-01T00:00:00Z",
        end_date="2023-01-03T00:00:00Z",
        polygon="[[-30,20],[-20,20],[-20,30],[-30,30],[-30,20]]",
        data="temperature",
    )
    save_raw(records, Path("data/raw/argovis_sample.csv"))
    print(f"Сохранено профилей: {len(records)}")