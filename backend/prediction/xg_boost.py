import xgboost as xgb
import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import xgboost as xgb
import numpy as np


def run_xgboost_model(transformed_data):
    loaded_model = xgb.Booster()
    loaded_model.load_model(r"backend\prediction\model\XGBoost_saved_model\xgboost_model.model")
    predicted_congestion = loaded_model.predict(xgb.DMatrix(transformed_data))
    return predicted_congestion