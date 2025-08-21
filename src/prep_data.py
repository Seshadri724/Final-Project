import argparse
import pandas as pd
from sklearn.datasets import fetch_california_housing

def main(out_path: str):
    # fetch from sklearn and save to CSV
    ds = fetch_california_housing(as_frame=True)
    df = ds.frame.rename(columns={"MedHouseVal": "target"})
    # No missing values in this dataset, but keep placeholder step
    df.to_csv(out_path, index=False)
    print(f"Saved dataset -> {out_path}  rows={len(df)} cols={len(df.columns)}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/cal_housing.csv")
    args = ap.parse_args()
    main(args.out)
