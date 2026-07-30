import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data.json"


def load_data() -> dict:
    if not DATA_FILE.exists():
        return {"students": [], "courses": [], "enrollments": []}

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data: dict) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
