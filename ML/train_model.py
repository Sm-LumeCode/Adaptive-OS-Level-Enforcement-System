import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATA ----------------
data = pd.read_csv("dataset.csv")

X = data.drop("label", axis=1)
y = data["label"]

# Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

# ---------------- PIPELINE ----------------
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(
        max_iter=2000,
        C=20,                    # 🔥 sharper boundary
        class_weight="balanced",
        solver="lbfgs"
    ))
])

# Train
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save
joblib.dump(pipeline, "mode_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("✅ Model trained successfully")
print(f"🎯 Validation accuracy: {accuracy * 100:.2f}%")
