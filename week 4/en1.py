class BankAccount:
    def __init__(self, balance):
        self.balance = balance   # public!

account = BankAccount(1000)

# Anyone can do this:
account.balance = -50000
print(account.balance)   # -50000 😱

# Nothing stopped it. The data is broken.


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₦{amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₦{amount}")
        else:
            print("Insufficient funds!")

    def get_balance(self):          # getter
        return self.__balance

account = BankAccount(1000)
account.deposit(500)                # Deposited ₦500
account.withdraw(200)               # Withdrew ₦200
print(account.get_balance())        # 1300





class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    # Getter
    def get_grade(self):
        return self.__grade

    # Setter with validation
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade! Must be 0-100.")

s = Student("Ada", 88)
print(s.get_grade())     # 88
s.set_grade(95)
print(s.get_grade())     # 95
s.set_grade(150)         # Invalid grade! Must be 0-100.
print(s.get_grade())     # 95 (unchanged)




class Wallet:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        # your code here
        pass

    def withdraw(self, amount):
        # your code here
        pass

    def get_balance(self):
        return self.__balance

# Test:
# w = Wallet()
# w.deposit(500)
# w.withdraw(200)
# print(w.get_balance())   # 300
# w.withdraw(10000)        # Should refuse