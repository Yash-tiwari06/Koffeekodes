class Bankacc:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited")
        else:
            print("amount is invalid")

    def withdraw(self, amount):
        if 0 < amoount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} is withdrwan")
        else:
            print("amount is invalid or exceeds balance")

acc = Bankacc("yash", 1000)
print(acc.get_balance())
acc.deposit(500)
print(acc.get_balance())