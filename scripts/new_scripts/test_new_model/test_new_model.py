import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load models
loaded_model = joblib.load(r"scripts/new_scripts/new_model/xgboost_model.joblib")
# loaded_model = joblib.load(r"scripts/new_scripts/new_model/random_forest_model.joblib")
#loaded_model = joblib.load(r"scripts/new_scripts/new_model/logistic_regession_model.joblib")
# loaded_model = joblib.load(r"scripts/new_scripts/new_model/gradient_boost_model.joblib")

# Load test data
test_data = pd.read_csv(r"scripts/dataset/test.csv")

# Choose feature
test_data_features = test_data[['arrival_hour', 'arrival_minute', 'stop_sequence_x', 'route_id', 'start_stop_id', 'end_stop_id']]

# Normalize the test data 
scaler = MinMaxScaler()
test_data_features_scaled = scaler.fit_transform(test_data_features)

# Make predictions 
predictions = loaded_model.predict(test_data_features_scaled).round()

result_df = pd.DataFrame({'Prediction': predictions, 'Actual': test_data['congestion_level']})
print("Predictions for the test data and actual congestion levels:")
print(result_df)