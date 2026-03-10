import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Step 1 : Load Dataset
def GetData(path):

    df = pd.read_csv(path)

    # remove index column
    df = df.drop(columns=['Unnamed: 0'])

    print("Dataset Loaded Successfully\n")
    print(df.head())

    return df


# Step 2 : Data Preparation
def PrepareData(df):

    le_weather = LabelEncoder()
    le_temp = LabelEncoder()
    le_play = LabelEncoder()

    df['Whether'] = le_weather.fit_transform(df['Whether'])
    df['Temperature'] = le_temp.fit_transform(df['Temperature'])
    df['Play'] = le_play.fit_transform(df['Play'])

    X = df[['Whether','Temperature']]
    Y = df['Play']

    return X,Y,le_weather,le_temp,le_play


# Step 3 : Train Model
def TrainModel(X,Y):

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X,Y)

    print("\nModel trained successfully")

    return model


# Step 4 : Test Model
def TestModel(model,le_weather,le_temp,le_play):

    weather = input("\nEnter Weather (Sunny/Overcast/Rainy): ")
    temp = input("Enter Temperature (Hot/Mild/Cool): ")

    weather = le_weather.transform([weather])[0]
    temp = le_temp.transform([temp])[0]

    prediction = model.predict([[weather,temp]])

    result = le_play.inverse_transform(prediction)

    print("\nPrediction :",result[0])


# Step 5 : Accuracy
def CheckAccuracy(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,Y,test_size=0.5,random_state=42
    )

    for k in range(1,6):

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train,Y_train)

        pred = model.predict(X_test)

        acc = accuracy_score(Y_test,pred)

        print("K =",k," Accuracy =",acc)


def main():

    path = "PlayPredictor.csv"

    df = GetData(path)

    X,Y,le_weather,le_temp,le_play = PrepareData(df)

    model = TrainModel(X,Y)

    TestModel(model,le_weather,le_temp,le_play)

    print("\nAccuracy Report:")
    CheckAccuracy(X,Y)


if __name__ == "__main__":
    main()