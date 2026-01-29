# Write a Python program to implement a class named Arithmetic with the following characteristics:
# The class should contain two instance variables: Value1 and Value2.
# Define a constructor (__init__) that initializes all instance variables to 0.
# Implement the following instance methods:
# Accept() – accepts values for Value1 and Value2 from the user.
# Addition() – returns the addition of Value1 and Value2.
# Subtraction() – returns the subtraction of Value1 and Value2.
# Multiplication() – returns the multiplication of Value1 and Value2.
# Division() – returns the division of Value1 and Value2 (handle division by zero properly).

class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter Value1 : "))
        self.Value2=int(input("Enter Value2 : "))

    def Add(self):
        return self.Value1 + self.Value2
    def Sub(self):
        return self.Value1 - self.Value2
    def Mul(self):
        return self.Value1 * self.Value2
    def Div(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            "Division by zero is not allowed. "
    
obj=Arithmetic()
obj.Accept()

print("Addition :",obj.Add())
print("Subtraction :",obj.Sub())
print("Multiplication :",obj.Mul())
print("Division :",obj.Div())