import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load Dataset
df = pd.read_csv("complaints.csv")

X = df["Complaint_Text"]
y = df["Category"]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Model
model = LogisticRegression(max_iter=1000)

model.fit(X_vectorized, y)

# Save Model
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model Saved Successfully")