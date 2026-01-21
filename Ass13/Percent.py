# Write a program which accepts marks and display grade.
# Condition example: >= 75-> Distinction   >= 60 ->First class   >= 50 ->Second class   < 50 -> fail


def percent(no):
    score=no

    if score >= 75:
        print("Distinction")
    elif score >= 60:
        print("First class")
    elif score >= 50:
        print("Second class")
    elif score < 50:
        print("Fail")
    else:
        print("Enter valid data")    

def main():

    print("Enter the Marks:")
    no=int(input())

    percent(no)

if __name__ == "__main__":
    main()