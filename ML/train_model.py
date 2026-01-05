import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

X = data.drop("label", axis=1)
y = data["label"]

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save model & encoder
joblib.dump(model, "mode_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("ML model trained successfully")
print(f"Validation accuracy: {accuracy * 100:.2f}%")