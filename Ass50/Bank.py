# ---------------------------------------------------------
# Bank Term Deposit Prediction (FINAL CODE)
# ---------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

# ---------------------------------------------------------
# STEP 1 : Load Dataset (FIXED)
# ---------------------------------------------------------

df = pd.read_csv("bank.csv", sep=';')   # IMPORTANT FIX

print("\nFirst 5 rows:\n", df.head())
print("\nInfo:\n")
print(df.info())
print("\nStatistics:\n", df.describe())

# ---------------------------------------------------------
# Handle 'unknown' values
# ---------------------------------------------------------

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].replace("unknown", df[col].mode()[0])

# Target distribution
plt.figure()
sns.countplot(x='y', data=df)
plt.title("Target Distribution")
plt.show()

# ---------------------------------------------------------
# STEP 2 : Preprocessing (BEST PRACTICE)
# ---------------------------------------------------------

# One Hot Encoding (better than LabelEncoder)
df = pd.get_dummies(df, drop_first=True)

# Features & Target
X = df.drop('y_yes', axis=1)   # y converted to y_yes
y = df['y_yes']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------------------------------------------------------
# STEP 3 : Train Test Split
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------------
# STEP 4 : Models
# ---------------------------------------------------------

lr = LogisticRegression(max_iter=1000)
knn = KNeighborsClassifier(n_neighbors=5)
rf = RandomForestClassifier(n_estimators=100)

lr.fit(X_train, y_train)
knn.fit(X_train, y_train)
rf.fit(X_train, y_train)

# ---------------------------------------------------------
# STEP 5 : Evaluation Function
# ---------------------------------------------------------

def evaluate_model(model, name):

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print(f"\n===== {name} =====")
    print("Accuracy:", accuracy_score(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)

    print("Classification Report:\n", classification_report(y_test, y_pred))

    roc_score = roc_auc_score(y_test, y_prob)
    print("ROC-AUC Score:", roc_score)

    # Confusion Matrix Plot
    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title(f"{name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)

    plt.figure()
    plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_score:.2f})")
    plt.plot([0,1], [0,1], linestyle='--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"{name} ROC Curve")
    plt.legend()
    plt.show()

# ---------------------------------------------------------
# STEP 6 : Evaluate Models
# ---------------------------------------------------------

evaluate_model(lr, "Logistic Regression")
evaluate_model(knn, "KNN")
evaluate_model(rf, "Random Forest")