# Write a lambda function which accept one number and return True if number is odd otherwise retun false.
 
Odd=lambda no : no % 2 == 1 

print("Enter the number :")
no=int(input())

ret=Odd(no)

print(ret)