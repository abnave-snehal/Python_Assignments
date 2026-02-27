# Write a single structured Python program that performs: 1)Dataset loading
# 2)Data analysis 3)Visualization 4)Train-test split 5)Model training 6)Prediction
# 7)Accuracy calculation 8)Confusion matrix generation
# Final conclusion: Your code should include proper comments explaining each step.

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score,confusion_matrix,ConfusionMatrixDisplay
)

# Load the dataset
dataSet="student_performance_ml.csv"
dataFrame=pd.read_csv(dataSet)

print("First 5 rows of dataset:")
print(dataFrame.head())

print("Dataset Information:")
print(dataFrame.info())

print("Statistical Summary:\n")
print(dataFrame.describe())

# Data Visualization
plt.figure()
dataFrame.boxplot(column="Attendance")
plt.title("Boxplot of Attendance")
plt.show()

# Train-Test Split
X=dataFrame.drop("FinalResult",axis=1)
y=dataFrame["FinalResult"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.2
)

# Model Training
model=DecisionTreeClassifier(max_depth=3)
model.fit(X_train,y_train)

# Prediction
y_pred=model.predict(X_test)

# Predict for a new student
students = pd.DataFrame([{
    "StudyHours": 6,
    "Attendance": 85,
    "PreviousScore": 66,
    "AssignmentsCompleted": 7,
    "SleepHours": 7
}])

new_predc=model.predict(students)
print("\nPrediction of new students: ",new_predc[0])

# Accuracy
train_acc=accuracy_score(y_train,model.predict(X_train))
test_acc=accuracy_score(y_test,y_pred)

print("\nTraining Accuracy: {:.2f}%".format(train_acc * 100))
print("Testing Accuracy: {:.2f}%".format(test_acc * 100))

# Confusion matrix
cm=confusion_matrix(y_test,y_pred)
disp=ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
plt.show()

# Final conclusion
print("\nFinal Conclusion:")
print("The Decision Tree model was trained to predict student performance.")
print("The model achieved {:.2f}% testing accuracy.".format(test_acc * 100))
print("The confusion matrix shows the correct and incorrect classifications.")
print("Based on the evaluation, the model performs well on this dataset.")