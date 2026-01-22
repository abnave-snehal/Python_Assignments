# Write a lambda function which accept two number and return Multiplication.
 
mulLambda=lambda no1,no2 : no1 * no2

print("Enter first number :")
no1=int(input())

print("Enter second number :")
no2=int(input())

ret=mulLambda(no1,no2)

print("Multiplication of two number is :",ret)