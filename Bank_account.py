# Bank Account — Create a BankAccount class with deposit(), withdraw(),
# and check_balance(). Prevent overdrafts
# and make the balance a private attribute.
class Bank_account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit Amount must be positive!")
            return
        self.__balance += amount
        print(f"Deposited {amount}. Remaining: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw Amount must be positive!")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdraw {amount}. Remaining: {self.__balance}")

    def check_balance(self):
        print(f"{self.owner}'s balance is {self.__balance}")

acc = Bank_account("Vijay", 10000)
acc.deposit(1500)
acc.withdraw(200)
acc.check_balance()
