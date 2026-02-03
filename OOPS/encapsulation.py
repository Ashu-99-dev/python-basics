# Wrapping up data and functions that operate on the data into a single unit is called encapsulation

class Account:
    def __init__(self, account_number, balance=0 ):
        self.account_number = account_number
        self.__balance = balance # private variable it will not access outside the class but we can access it using getter and setter method

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} credited to the account: {self.account_number}")
            self.show_balance()
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} debited from the account: {self.account_number}")
            self.show_balance()
        else:
            print("Invalid withdrawal amount")

    def show_balance(self):
        print(f"The balance is {self.__balance}")


s1 = Account(123456789, 1000)
s1.show_balance()

s1.deposit(500)
s1.withdraw(200)
s1.account_number = 1234567890
print(s1.account_number)
