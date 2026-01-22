# Write a lambda function which accepts one number and return cube of that number.

Cube=lambda no : no * no * no


print("Enter the number : ")
no=int(input())

ret=Cube(no)
print("Cube of a number is : ",ret)