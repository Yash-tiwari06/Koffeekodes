class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} is credited!")
        else:
            print("Invalid amount!")
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} is debited!")
        else:
            print("Invalid amount !")
acc = BankAccount("yash", 10000)
print(acc.deposit(28000))
print(acc.get_balance())
print(acc.withdraw(5000))
print(acc.get_balance())

