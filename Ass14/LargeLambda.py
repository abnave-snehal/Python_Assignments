# Write a lambda function which accept three numbers and return largest number.
 
largeLambda=lambda no1,no2,no3 : no1 if (no1 > no2 and no1 >no3 ) else ( no2 if no2 > no3 else no3 ) 

print("Enter first number :")
no1=int(input())

print("Enter second number :")
no2=int(input())

print("Enter second number :")
no3=int(input())

ret=largeLambda(no1,no2,no3)

print("Largest number is :",ret)