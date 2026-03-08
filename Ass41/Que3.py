import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def StudentResultPredictor():

    data = {
        "StudyHours": [2,5,6,1],
        "Attendance": [60,80,85,50],
        "Result": ["Fail","Pass","Pass","Fail"]
    }

    df = pd.DataFrame(data)

    X = df[["StudyHours","Attendance"]]
    Y = df["Result"]

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X,Y)

    hours = int(input("Enter Study Hours: "))
    attendance = int(input("Enter Attendance: "))

    # Fix
    test_data = pd.DataFrame([[hours, attendance]], columns=["StudyHours","Attendance"])

    prediction = model.predict(test_data)

    print("Predicted Result:", prediction[0])


def main():
    StudentResultPredictor()

if __name__ == "__main__":
    main()