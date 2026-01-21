# Write a program which accepts lenght and width of a rectangle and print area.

def areaRect(l,w):
    Area=None

    Area= l * w
    return Area

def main():
    print("Enter the length of a rectangle:")
    l=int(input())

    print("Enter the width of a rectangle:")
    w=int(input())

    result=areaRect(l,w)
    print("Area of a rectangle is:", result)

if __name__ == "__main__":
    main()