# Write a lambda function which accepts two numbers and return maximum of a number.

Max=lambda no1,no2 : no1 if no1 > no2 else no2


print("Enter first number : ")
no1=int(input())

print("Enter second number : ")
no2=int(input())

ret=Max(no1,no2)
print("Maximum of a number is : ",ret)