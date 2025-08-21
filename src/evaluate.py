import argparse
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score

def main(data_path, model_path):
    # Load data
    data = pd.read_csv(data_path)
    X = data.drop("target", axis=1)
    y = data["target"]

    # Load trained model
    model = joblib.load(model_path)

    # Predict
    y_pred = model.predict(X)

    # Metrics
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    print(f"✅ Evaluation Results:")
    print(f"MSE: {mse:.4f}")
    print(f"R2: {r2:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True, help="Path to dataset CSV")
    parser.add_argument("--model", type=str, required=True, help="Path to trained model")
    args = parser.parse_args()

    main(args.data, args.model)
