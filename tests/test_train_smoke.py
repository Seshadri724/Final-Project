from pathlib import Path
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

def test_smoke_training():
    ds = fetch_california_housing(as_frame=True)
    df = ds.frame.rename(columns={"MedHouseVal": "target"})
    y = df["target"]
    X = df.drop(columns=["target"])
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([("scaler", StandardScaler()), ("reg", LinearRegression())])
    pipe.fit(Xtr, ytr)
    r2 = r2_score(yte, pipe.predict(Xte))
    assert r2 > 0.4  # sanity threshold
