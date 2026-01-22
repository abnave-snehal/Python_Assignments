# Write a program which display first 10 even number on a screen.
# Output: 2 4 6 8 10 12 14 16 20

def even():
    print("First 10 Even numbers are : ")
    for i in range(2,22,2):
        print(i, end=" ")

def main():

    even()

if __name__ == "__main__":
    main()