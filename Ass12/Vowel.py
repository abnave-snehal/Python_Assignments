# Write a program which accepts one character and check whether it is vowel or consonant.

# Input:a Output:Vowel

def chkVowel(ch):
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        print("It is vowel")
    else:
        print("It is consonant")    

def main():
    ch=(input("Enter the character : "))

    ch=chkVowel(ch)

if __name__ == "__main__":
    main()