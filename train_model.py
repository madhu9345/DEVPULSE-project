import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("developer_productivity.csv")

X = df[['typing_speed', 'pause_time', 'errors']]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('dev_model.pkl', 'wb'))

print("✅ Model Trained and Saved as dev_model.pkl")
