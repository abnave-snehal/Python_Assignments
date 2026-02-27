# 4. Generate confusion matrix using sklearn. Display it using ConfusionMatrixDisplay.
# Explain clearly: 1)True Positive 2)True Negative 3)False Positive 4)False Negative

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,confusion_matrix,ConfusionMatrixDisplay
)

dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

X=dataFrame.drop("FinalResult",axis=1)
y=dataFrame["FinalResult"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=DecisionTreeClassifier()

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

cm=confusion_matrix(y_test,y_pred)

print("Confusion Matrix : ",cm)

disp=ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

plt.title("Confusion Matrix")
plt.show()