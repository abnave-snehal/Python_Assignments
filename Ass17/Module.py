import Arithmatic

print("Inside Client : ",__name__)

print("Enter first no : ")
no1=int(input())

print("Enter second no : ")
no2=int(input())

result=Arithmatic.Add(no1,no2)
print("Addition is : ",result)

result=Arithmatic.Sub(no1,no2)
print("Subtraction is : ",result)

result=Arithmatic.Mul(no1,no2)
print("Multiplication is : ",result)

result=Arithmatic.Div(no1,no2)
print("Division is : ",result)



