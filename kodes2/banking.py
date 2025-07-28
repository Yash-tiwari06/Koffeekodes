class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("successfully deposited",amount)
        return self.balance
        
        
    def withdraw(self, amount):
        self.balance -= amount
        print("successfully credited", amount)
        return self.balance

account = BankAccount("Arpit", 50000)
account.deposit(500)
account.withdraw(5000)
account.get_balance()
print(self

    