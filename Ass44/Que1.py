# Machine Learning Assignment
# Linear Regression on Advertisement Dataset

# Step 1: Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 2: Load the dataset
data = pd.read_csv("Advertising.csv")

# Display first 5 rows
print("Dataset Preview:\n")
print(data.head())

# Step 3: Prepare the data

# Independent variables (features)
X = data[['TV', 'radio', 'newspaper']]

# Dependent variable (target)
y = data['sales']

# Step 4: Split dataset into training and testing (50% - 50%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)

# Step 5: Create Linear Regression model
model = LinearRegression()

# Step 6: Train the model
model.fit(X_train, y_train)

print("\nModel Training Completed")

# Step 7: Predict sales
y_pred = model.predict(X_test)

# Step 8: Display predicted and expected values
print("\nPredicted vs Expected values:\n")

for i in range(len(y_pred)):
    print("Predicted:", round(y_pred[i],2), "Expected:", y_test.iloc[i])

# Step 9: Model accuracy
accuracy = model.score(X_test, y_test)

print("\nModel Accuracy (R2 Score):", accuracy)