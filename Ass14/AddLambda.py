# Write a lambda function which accept two number and return Addition.
 
addLambda=lambda no1,no2 : no1 + no2

print("Enter first number :")
no1=int(input())

print("Enter second number :")
no2=int(input())

ret=addLambda(no1,no2)

print("Addition of two number is :",ret)