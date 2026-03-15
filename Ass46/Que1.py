import pandas as pd
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "StudyHours": [1,2,3,4,5],
    "Marks": [50,55,60,65,70]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Separate input and output
X = df[["StudyHours"]]   # Independent variable
y = df["Marks"]          # Dependent variable

# Create model
model = LinearRegression()

# Train the model
model.fit(X,y)

# Print coefficient and intercept
print("\nCoefficient :",model.coef_[0])
print("Intercept :",model.intercept_)

# Predict marks for 6 study hours
predicted_marks = model.predict([[6]])

print("\nPredicted Marks for 6 study hours :",predicted_marks[0])