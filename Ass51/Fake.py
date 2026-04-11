# Import required libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -------------------------------
# Part 1: Data Preprocessing
# -------------------------------

# Load datasets
fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

# Add labels
fake_df["label"] = 0   # Fake
true_df["label"] = 1   # Real

# Combine datasets
df = pd.concat([fake_df, true_df], axis=0)

# Shuffle data
df = df.sample(frac=1).reset_index(drop=True)

# Drop null values
df = df.dropna()

# Use only text column (you can also combine title + text)
df["content"] = df["title"] + " " + df["text"]

X = df["content"]
y = df["label"]

# -------------------------------
# Part 2: Feature Extraction
# -------------------------------

tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)

X_tfidf = tfidf.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

# -------------------------------
# Part 3: Model Training
# -------------------------------

# Individual models
lr = LogisticRegression()
dt = DecisionTreeClassifier()

# Train individual models
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)

# Predictions
lr_pred = lr.predict(X_test)
dt_pred = dt.predict(X_test)

# Voting Classifier - Hard Voting
hard_voting = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='hard'
)

hard_voting.fit(X_train, y_train)
hard_pred = hard_voting.predict(X_test)

# Voting Classifier - Soft Voting
soft_voting = VotingClassifier(
    estimators=[('lr', lr), ('dt', dt)],
    voting='soft'
)

soft_voting.fit(X_train, y_train)
soft_pred = soft_voting.predict(X_test)

# -------------------------------
# Part 4: Evaluation
# -------------------------------

print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_pred))
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))
print("Hard Voting Accuracy:", accuracy_score(y_test, hard_pred))
print("Soft Voting Accuracy:", accuracy_score(y_test, soft_pred))

print("\nConfusion Matrix - Logistic Regression:\n", confusion_matrix(y_test, lr_pred))
print("\nConfusion Matrix - Decision Tree:\n", confusion_matrix(y_test, dt_pred))
print("\nConfusion Matrix - Hard Voting:\n", confusion_matrix(y_test, hard_pred))
print("\nConfusion Matrix - Soft Voting:\n", confusion_matrix(y_test, soft_pred))

print("\nClassification Report (Soft Voting):\n")
print(classification_report(y_test, soft_pred))