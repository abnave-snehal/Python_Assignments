# Write a Python program to implement a class named Demo with the following specifications:
# The class should contain two instance variables: no1 and no2.
# The class should contain one class variable named Value.
# Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
# Implement two instance methods:
# Fun() – displays the values of instance variables no1 and no2.
# Gun() – displays the values of instance variables no1 and no2.

# Obj1 = Demo(11, 21)
# Obj2 = Demo(51, 101)

# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()


class Demo:
    Value=50                    # Class Variable   
    def __init__(self,a,b):
        self.no1=a              # Instance variable
        self.no2=b              # Instance variable
    def Fun(self):
        print("Value of instance variable fun() :",self.no1,self.no2)

    def Gun(self):
        print("Value of instance variable gun() :",self.no1,self.no2)

obj1=Demo(11,21)
obj2=Demo(51,101)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()