# Write a lambda function which accept one number and return True if divisible by 5.
 
Divisible5=lambda no : no % 5 == 0

print("Enter the number :")
no=int(input())

ret=Divisible5(no)

print(ret)