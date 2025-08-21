# California Housing Capstone (Regression)

End‑to‑end MLOps pipeline to predict California house prices.

## Stack
- Python 3.10+
- scikit-learn, pandas, numpy
- MLflow (local tracking)
- FastAPI + Uvicorn
- Docker
- GitHub Actions (CI)
- Optional: Prometheus metrics, SQLite logging

## Quickstart

```bash
# 1) Create venv and install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2) Prepare data
python -m src.prep_data --out data/cal_housing.csv

# 3) Train models (logs to mlruns/ with MLflow)
python -m src.train --data data/cal_housing.csv --out models/model.joblib

# 4) Evaluate (prints metrics)
python -m src.evaluate --data data/cal_housing.csv --model models/model.joblib

# 5) Run API
uvicorn api.main:app --reload
```

### Docker
```bash
docker build -t cal-housing-api .
docker run -p 8000:8000 cal-housing-api
```

### CI
A lightweight GitHub Actions workflow runs flake8 + unit tests and builds the Docker image.

### Endpoints
- `GET /health`
- `POST /predict`

Example payload:
```json
{
  "longitude": -122.05,
  "latitude": 37.37,
  "housing_median_age": 27.0,
  "total_rooms": 3885.0,
  "total_bedrooms": 661.0,
  "population": 1537.0,
  "households": 606.0,
  "median_income": 6.6085
}
```
