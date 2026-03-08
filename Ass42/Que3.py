import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def SalaryPrediction():

    # Dataset
    experience = np.array([1,2,3,4,5]).reshape(-1,1)
    salary = np.array([20000,25000,30000,35000,40000])

    # Train model
    model = LinearRegression()
    model.fit(experience, salary)

    # Predict salary for 6 years
    predicted_salary = model.predict([[6]])

    print("Predicted Salary for 6 Years Experience: ₹", int(predicted_salary[0]))

    # Plot data points
    plt.scatter(experience, salary)

    # Plot regression line
    plt.plot(experience, model.predict(experience))

    plt.title("Experience vs Salary")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.grid(True)

    plt.show()


def main():
    SalaryPrediction()


if __name__ == "__main__":
    main()