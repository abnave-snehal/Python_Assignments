import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1 : Create dataset
data = {
    "StudyHours":[1,2,3,4,5],
    "Marks":[50,55,60,65,70]
}

df = pd.DataFrame(data)

print("Dataset :")
print(df)

# Step 2 : Separate input and output
X = df[["StudyHours"]]
y = df["Marks"]

# Step 3 : Create model
model = LinearRegression()

# Step 4 : Train the model
model.fit(X,y)

# Step 5 : Print coefficient and intercept
print("\nCoefficient :",model.coef_[0])
print("Intercept :",model.intercept_)

# Question 8 : Predict marks for 6 study hours
hours = [[6]]
predicted_marks = model.predict(hours)

print("\nPredicted Marks for 6 study hours :",predicted_marks[0])