import argparse
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def main(data_path, out_path):
    # Load data
    df = pd.read_csv("data/cal_housing.csv")
    target_col = "target"
    X = df.drop(columns=[target_col])
    y = df[target_col]
    print("✅ Data loaded successfully!")
    print("Columns:", df.columns.tolist())
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)





    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Build pipeline
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", LinearRegression())
    ])

    # Train model
    pipeline.fit(X_train, y_train)

    # ✅ Set MLflow local tracking
    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment("california-housing-regression")

    with mlflow.start_run():
        mlflow.log_param("model", "LinearRegression")
        mlflow.log_param("scaler", "StandardScaler")
        mlflow.sklearn.log_model(pipeline, "model")

    # ✅ Save model with joblib
    joblib.dump(pipeline, out_path)
    print(f"Model saved at {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True, help="Path to dataset CSV")
    parser.add_argument("--out", type=str, required=True, help="Path to save model")
    args = parser.parse_args()

    main(args.data, args.out)




def main(data_path, out_path):
    print("👉 Debug: entered main()")
    print("👉 Debug: loading CSV from:", data_path)

    import os
    print("👉 Debug: absolute path =", os.path.abspath(data_path))

    data = pd.read_csv(data_path)
    print("👉 Debug: CSV loaded successfully")
    print("👉 Columns in dataset:", data.columns.tolist())
    print("👉 First 5 rows:")
    print(data.head())

