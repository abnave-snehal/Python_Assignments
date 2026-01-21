# Write a program which accepts radius of a circle and print area of circel.

def areaCircle(r):
    
    radius= 3.14 * ( r * r)
    return radius

def main():
    print("Enter the radius of a circel :")
    r=float(input())


    result=areaCircle(r)
    print("Area of a circle is:", result)

if __name__ == "__main__":
    main()