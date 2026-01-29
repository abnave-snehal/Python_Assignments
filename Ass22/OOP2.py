# Write a Python program to implement a class named Circle with the following requirements:
# The class should contain three instance variables: Radius, Area, and Circumference.
# The class should contain one class variable named PI, initialized to 3.14.
# Define a constructor (__init__) that initializes all instance variables to 0.0.
# Implement the following instance methods:
# Accept() – accepts the radius of the circle from the user.
# CalculateArea() – calculates the area of the circle and stores it in the Area variable.
# CalculateCircumference() – calculates the circumference of the circle and stores it in the Circumference variable.
# Display() – displays the values of Radius, Area, and Circumference.
# Create multiple objects of the Circle class and invoke all the instance methods for each object.


class Circle:
    PI=3.14                         # Class Variable
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circum=0.0

    def Accept(self):
        self.Radius=float(input("Enter the number : "))

    def CalculateArea(self):
        self.Area=Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circum=2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius",self.Radius)
        print("Area",self.Area)
        print("Circumfarance",self.Circum)

obj1=Circle()
obj2=Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()
    




