# 1. After training the Decision Tree model, use: model.feature_importances_
# Display importance score of each feature.
# Which feature contributes the most in predicting FinalResult?
# Which feature contributes the least?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

X=dataFrame.drop("FinalResult",axis=1)
y=dataFrame["FinalResult"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.2
)

model=DecisionTreeClassifier(max_depth=3,random_state=42)
model.fit(X_train,y_train)

importance=model.feature_importances_

print("Features Importants")
for features,importance in zip(X.columns,importance):
    print(f"{features}:{importance:.4f}")

most_imp=X.columns[importance.argmax()]
least_imp=X.columns[importance.argmin()]

print("\nMost Important Feature:", most_imp)
print("Least Important Feature:", least_imp)