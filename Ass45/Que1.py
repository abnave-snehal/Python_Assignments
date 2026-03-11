from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Step 1: Get data

data=load_wine()
X=data.data
Y=data.target

# Step 2: Prepare data
X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Step 3: Train model
model=DecisionTreeClassifier()
model.fit(X_train,Y_train)

# Step 4: Test model
y_pred=model.predict(X_test)

# Step 5: Calculate Accuracy
accuracy=accuracy_score(Y_test,y_pred)

print("Accuracy is : ",accuracy)