import random
import json

print("---Defining account class---")


class Account:
    def __init__(self, holder_name, initial_deposit):
        print(f"DEBUG: Creating account for {holder_name}")

        # ---attributes---
        self.account_holder_name = holder_name

        self.account_number = str(random.randint(10000, 99999))

        if initial_deposit < 0:
            print("Warning, you are broke as shit")
            self.balance = 0.0
        else:
            self.balance = float(initial_deposit)

        print(
            f"DEBUG: account {self.account_number} created for  {self.account_holder_name}. The initial balance is {self.balance}")

    def check_balance(self):
        print(
            f"\n---Balance for account #{self.account_number} ({self.account_holder_name})---")
        print(f"The current balance is {self.balance}")
        print("----------------------------------------")

    def deposit(self, amount):

        if amount <= 0:
            print("deposit amount must be positive")
            return False

        self.balance += float(amount)
        print(f"\nDeposited ${amount:.2f}.")
        print(
            f"New balance for account {self.account_number} is ${self.balance}")
        return True

    def withdraw(self, amount):
        if amount < 0:
            print("withdrawal number must be positive")
            return False
        if amount > self.balance:
            print(
                f"Your withdrawal amount of {amount} is greater than your balancec of {self.balance}")
            print("insufficient funds, withdrawal failed")
            return False
        else:
            self.balance -= float(amount)
            print("Withdrawal in processing")
            print(
                f"You have withdrawn ${amount}, your remaining balance is {self.balance}")
            return True

    def add_interest(self, rate):
        if rate <= 0:
            print("interest rate must be greater than 0")
            return False
        interest_amount = self.balance * rate
        self.balance += interest_amount

        print(
            f"Interest payment of {interest_amount:.2f} added. new balance is {self.balance:.2f}")
        return True

    def __str__(self):
        return f"Account Holder: {self.account_holder_name}\nAccount Number: {self.account_number}\nBalance: ${self.balance:.2f}"


class SavingsAccount(Account):

    def __init__(self, holder_name, initial_deposit=0.0, withdrawal_limit=1000.0):
        print(f"DEBUG: created savings account for {holder_name}")
        super().__init__(holder_name, initial_deposit)

        # attributes specific to this subclass
        self.withdrawal_limit = float(withdrawal_limit)
        print(
            f"DEBUG: savings account set with withdrawal limit: ${self.withdrawal_limit}")

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(
                f"The amount ${amount} is larger than the withdrawal limit of ${self.withdrawal_limit}")
            return False

        return super().withdraw(amount)


print("---Savings account class defined---")
print("---account class defined---")
acc1 = Account("Jesus Christ", 1000)
acc2 = Account(holder_name="Bob Marley", initial_deposit=2000)

print("\n---Account details---")
print(
    f"Account holder: {acc1.account_holder_name}, account number: {acc1.account_number}, balance: {acc1.balance}")
print(
    f"Account holder: {acc2.account_holder_name}, account number: {acc2.account_number}, balance: {acc2.balance}")
print("\n---Account details---")
print("\n--- Creating Accounts (Regular and Savings) ---")
# Keep your existing accounts if you like
acc1 = Account(holder_name="Alice", initial_deposit=500.50)
# Create a SavingsAccount instance
sav_acc1 = SavingsAccount(holder_name="Bob (Savings)",
                          initial_deposit=2000.0, withdrawal_limit=500.0)

print("\n--- Testing Withdrawals ---")

# Regular account - no limit other than balance
print("\n* Regular Account (Alice):")
acc1.check_balance()
acc1.withdraw(400.0)  # Should succeed
acc1.withdraw(150.0)  # Should fail (insufficient funds)
acc1.check_balance()

# Savings account - has withdrawal limit
print("\n* Savings Account (Bob):")
sav_acc1.check_balance()
sav_acc1.withdraw(400.0)  # Should succeed (below limit)
# Should FAIL (above limit, even though balance is sufficient)
sav_acc1.withdraw(600.0)
# Should succeed (below limit, assuming balance after previous withdrawal)
sav_acc1.withdraw(1200.0)
sav_acc1.check_balance()

# Test __str__ on both (inherited __str__ still works for SavingsAccount)
print("\n--- String Representation ---")
print(acc1)
print("-" * 20)
print(sav_acc1)  # Uses the __str__ from the Account class!
running = True

# while running:
