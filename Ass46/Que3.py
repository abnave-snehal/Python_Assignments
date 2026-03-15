import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1 : Create dataset
data = {
    "StudyHours":[1,2,3,4,5],
    "SleepHours":[7,6,7,6,8],
    "Marks":[50,55,60,65,70]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Step 2 : Separate features and target
X = df[["StudyHours","SleepHours"]]
y = df["Marks"]

# Step 3 : Create model
model = LinearRegression()

# Step 4 : Train model
model.fit(X,y)

# Step 5 : Print coefficients
print("\nCoefficient for StudyHours :",model.coef_[0])
print("Coefficient for SleepHours :",model.coef_[1])

# Step 6 : Print intercept
print("Intercept :",model.intercept_)