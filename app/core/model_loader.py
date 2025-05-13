from joblib import load
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler
from catboost import CatBoostRegressor

MODEL_PATH = Path(__file__).resolve().parent.parent.parent / "models"

model: CatBoostRegressor = load(MODEL_PATH / "model_cb.joblib")
scaler: MinMaxScaler = load(MODEL_PATH / "scaler.joblib")
enc: dict = load(MODEL_PATH / "mean_encoder.joblib")
