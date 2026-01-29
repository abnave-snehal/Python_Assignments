# Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables: Name (Account holder name) , Amount (Account balance)
# The class should contain one class variable: ROI (Rate of Interest), initialized to 10.5
# Define a constructor (__init__) that accepts Name and initial Amount.
# Implement the following instance methods: Display() – displays account holder name and current balance.
# Deposit() – accepts an amount from the user and adds it to the balance.
# Withdraw() – accepts an amount from the user and subtracts it from the balance
# (ensure withdrawal amount does not exceed available balance).
# CalculateInterest() – calculates interest using the formula: Interest = Amount * ROI / 100
# Create multiple objects of the BankAccount class and invoke all instance methods.

class BankAccount:
    ROI=10.5
    
    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount
    
    def Display(self):
        print("Account Holder name",self.Name)
        print("Account Balance : ",self.Amount)

    def Deposite(self):
        deposit=int(input("Enter the amount to deposite : "))
        self.Amount+=deposit
        print("Amount Deposite Successfully")

    def Withdraw(self):
        withdraw=int(input("Enter Amount for withdraw : "))
        if withdraw <= self.Amount:
            self.Amount -= withdraw
            print("Amount Withdraw Successfully : ")
        else:
            print("Insufficient Balance : ")
    
    def CalculateInterest(self):
        interest = self.Amount * BankAccount.ROI / 100
        return interest

obj1=BankAccount("Snehal Abnave",2000)


obj1.Display()
obj1.Deposite()
obj1.Withdraw()
print("Interest : ",obj1.CalculateInterest())

print("____________________")

obj2=BankAccount("Avani Yogesh",500)
obj2.Display()
obj2.Deposite()
obj2.Withdraw()
print("Interest : ",obj2.CalculateInterest())