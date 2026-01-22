# Write a lambda function which accept one number and return True if number is even otherwise false.
 
Even=lambda no : no % 2 == 0 

print("Enter the number :")
no=int(input())

ret=Even(no)

print(ret)