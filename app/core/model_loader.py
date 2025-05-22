from joblib import load
from pathlib import Path
from xgboost import XGBRegressor

MODEL_PATH = Path(__file__).resolve().parent.parent.parent / "models"

model_pipeline: XGBRegressor = load(MODEL_PATH / "xgboost_pipeline.joblib")
