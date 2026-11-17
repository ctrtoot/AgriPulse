"""Lightweight integrity checks for the AgriPulse demo data package."""
from __future__ import annotations
import csv
import gzip
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    summary = load_json(DATA / "summary.json")
    geo = load_json(DATA / "grid.geojson")
    with gzip.open(DATA / "details.json.gz", "rt", encoding="utf-8") as f:
        details = json.load(f)

    features = geo.get("features", [])
    expected = int(summary["grid_count"])
    assert geo.get("type") == "FeatureCollection", "grid.geojson must be a FeatureCollection"
    assert len(features) == expected, f"GeoJSON has {len(features)} features; expected {expected}"
    assert len(details) == expected, f"details has {len(details)} records; expected {expected}"

    ids = [x.get("properties", {}).get("grid_id") for x in features]
    assert None not in ids, "A feature is missing grid_id"
    assert len(ids) == len(set(ids)), "Duplicate grid_id in GeoJSON"
    assert set(ids) == set(details), "GeoJSON and details grid_id sets do not match"

    for grid_id, record in details.items():
        for crop in ("maize", "peanut"):
            classes = record.get(crop)
            assert isinstance(classes, list) and len(classes) == 12, f"{grid_id}: {crop} must have 12 monthly classes"
            assert all(v in {"S1", "S2", "S3", "N", None} for v in classes), f"{grid_id}: invalid {crop} class"

    with (DATA / "Suitability_Summary.csv").open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 24, f"Expected 24 crop-month summary rows, got {len(rows)}"
    for row in rows:
        total = sum(int(row[k]) for k in ("S1", "S2", "S3", "N", "missing"))
        assert total == expected, f"Summary total mismatch: {row}"

    print("PASS: GeoJSON/detail IDs match; 22,160 grid cells; 12 months per crop; 24 summary rows.")


if __name__ == "__main__":
    main()
