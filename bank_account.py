class BankAccount:
    def __init__(self, interest, balance=0):
        self.interest = interest
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance*self.interest
        return self

test = BankAccount(0.01, 100)
test.deposit(500).deposit(500).deposit(500).withdraw(1200).yield_interest().display_account_info()

test2 = BankAccount(.02)
test2.deposit(1000).deposit(500).withdraw(50).withdraw(12).withdraw(4).withdraw(100).yield_interest().display_account_info()
