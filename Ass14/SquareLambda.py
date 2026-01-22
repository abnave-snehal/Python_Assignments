# Write a lambda function which accepts one number and return square of that number.

Square=lambda no : no * no


print("Enter the number : ")
no=int(input())

ret=Square(no)
print("Square of a number is : ",ret)