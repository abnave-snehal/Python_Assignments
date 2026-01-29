# Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable: Value
# Define a constructor (__init__) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# CheckPrime() – returns True if the number is prime, otherwise returns False.
# CheckPerfect() – returns True if the number is perfect, otherwise returns False.
# Factors() – displays all factors of the number.
# SumFactors() – returns the sum of all factors of the number.
# Create multiple objects of the Numbers class and invoke all the instance methods.

class Numbers:
    def __init__(self):
        self.Value=int(input("Enter the Number : "))
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        sum_Fact=0
        for i in range(1,self.Value):
            if self.Value % i ==0:
                sum_Fact+=i
        return sum_Fact == self.Value
    
    def Factors(self):
        print("Factors of ",self.Value, "are : ")
        for i in range(1,self.Value+1):
            if self.Value % i == 0 :
                print(i,end=" ")
    def SumFact(self):
        total=0
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                total+=i
        return total

obj1=Numbers()
obj2=Numbers()

print("Is Prime :",obj1.ChkPrime())
print("Is Perfect : ",obj1.ChkPerfect())

obj1.Factors()
print("Sum of Factors : ",obj1.SumFact())

print("____________________________")

print("Is Prime :",obj2.ChkPrime())
print("Is Perfect : ",obj2.ChkPerfect())

obj2.Factors()
print("Sum of Factors : ",obj2.SumFact())
