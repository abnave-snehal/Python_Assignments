# ---------------------------------------------------------
# Diabetes Prediction Project
# ---------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ---------------------------------------------------------
# STEP 1 : Load Dataset
# ---------------------------------------------------------

# Replace with your dataset path
df = pd.read_csv("diabetes.csv")

print("\nFirst 5 Rows:\n", df.head())

print("\nInfo:\n")
print(df.info())

print("\nNull Values:\n", df.isnull().sum())

print("\nStatistics:\n", df.describe())


# ---------------------------------------------------------
# STEP 2 : EDA
# ---------------------------------------------------------

# Target distribution
plt.figure()
sns.countplot(x='Outcome', data=df)
plt.title("Target Distribution")
plt.show()

# Histograms
df.hist(figsize=(10,8))
plt.show()

# Boxplot (outliers)
plt.figure(figsize=(10,6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()


# ---------------------------------------------------------
# STEP 3 : Data Preprocessing
# ---------------------------------------------------------

# Replace 0 with median (important columns)
cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in cols:
    df[col] = df[col].replace(0, df[col].median())

# Features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)


# ---------------------------------------------------------
# STEP 4 : Model Building
# ---------------------------------------------------------

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)


# ---------------------------------------------------------
# STEP 5 : Evaluation Function
# ---------------------------------------------------------

def evaluate_model(model, X_test, y_test, name):

    y_pred = model.predict(X_test)

    print(f"\n===== {name} =====")
    print("Accuracy:", accuracy_score(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)

    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Plot confusion matrix
    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title(f"{name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    return y_pred


# Evaluate models
lr_pred = evaluate_model(lr, X_test, y_test, "Logistic Regression")
knn_pred = evaluate_model(knn, X_test, y_test, "KNN")


# ---------------------------------------------------------
# STEP 6 : Final Prediction & Save CSV
# ---------------------------------------------------------

# Use best model (example: Logistic Regression)
final_predictions = lr.predict(X_test)

# Save to CSV
output = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": final_predictions
})

output.to_csv("predictions.csv", index=False)

print("\nPredictions saved to predictions.csv")