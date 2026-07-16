import os
import joblib
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load embeddings and labels
embeddings = np.load("dataset/embeddings/embeddings.npy")
labels = np.load("dataset/embeddings/labels.npy")

print("Embeddings Shape :", embeddings.shape)
print("Labels Shape :", labels.shape)

# Encode labels
encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(labels)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    embeddings,
    encoded_labels,
    test_size=0.2,
    random_state=42
)

# Train SVM
print("\nTraining SVM Model...")

model = SVC(
    kernel="linear",
    probability=True
)

model.fit(X_train, y_train)

print("Model Trained Successfully!")

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy : {accuracy*100:.2f}%")

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

# Save Model
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/svm_model.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")

print("\nModel Saved Successfully!")