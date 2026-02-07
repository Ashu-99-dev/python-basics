# Wrapping up data and functions that operate on the data into a single unit is called encapsulation
import time

class Account:
    def __init__(self, account_name, balance=0 ):
        self.account_name = account_name
        self.__balance = balance # private variable it will not access outside the class but we can access it using getter and setter method

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} credited to account: {self.account_name}")
            self.show_balance()
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} debited from the account: {self.account_name}")
            self.show_balance()
        else:
            print(f"Sorry, account: {self.account_name} has only balance of ₹{self.__balance}")

    def show_balance(self):
        print(f"Account: '{self.account_name}' has balance of ₹{self.__balance}")

    def transfer(self, amount, target_account):
        if 0 < amount <= self.__balance:
            print("Beginning transfer process")
            print("Withdrawing.....")
            time.sleep(1)
            print("Withdrawn completed")
            self.withdraw(amount)
            print("Depositing amount......")
            time.sleep(2)
            print("Deposit completed")
            target_account.deposit(amount)
            print(f"₹{amount} transferred from {self.account_name} to {target_account.account_name}")
            self.show_balance()
            target_account.show_balance()
        else:
            print(f"Sorry, account: {self.account_name} has only balance of ₹{self.__balance}")


class InterestRewardAcc(Account):
    def deposit(self, amount):
        # Add 5% interest to the deposit amount and call parent's deposit
        interest_amount = amount * 1.05
        print(f"🎉 Interest reward: ₹{amount} + 5% interest = ₹{interest_amount}")
        super().deposit(interest_amount)  # Call parent's deposit method

class SavingAcc(InterestRewardAcc):
    def __init__(self, account_name, balance=0):
        super().__init__(account_name, balance)
        self.fee = 5

    def withdraw(self, amount):
        # Add fee to the withdrawal amount and call parent's withdraw
        total_amount = amount + self.fee
        print(f"💸 Withdrawal fee: ₹{self.fee} applied")
        super().withdraw(total_amount)  # Call parent's withdraw method