import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

print("Loading data...")
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

print("Training Random Forest model...")
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, y)

print("Saving model to model.pkl...")
joblib.dump(regressor, 'model.pkl')

print("Model trained and saved successfully.")
