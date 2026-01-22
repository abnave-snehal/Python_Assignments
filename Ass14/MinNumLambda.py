# Write a lambda function which accepts two numbers and return minimum of a number.

Min=lambda no1,no2 : no1 if no1 < no2 else no2


print("Enter first number : ")
no1=int(input())

print("Enter second number : ")
no2=int(input())

ret=Min(no1,no2)
print("Minimum of a number is : ",ret)