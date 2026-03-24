# OOPS
# QUES-1 CREATE AN ABSTRACT CLASS
# from abc import ABC, abstractmethod

# class Account(ABC):
#     def __init__(self, account_number, holder_name, balance):
#         self.__account_number = account_number
#         self.__holder_name = holder_name
#         self.__balance = balance

#     def deposite(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited : {amount}")
#         else:
#             print("Invalid deposite amount")
    
#     def Withdrawl(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount} withdraw sucessfully")
#         else:
#             print("Insufficient amount")
    
#     def get_balance(self):
#         return self.__balance
    
#     @abstractmethod
#     def calculate_interest(self):
#         pass

# class SavingsAccount(Account):
#     def calculate_interest(self):
#         interest = self.get_balance() * 0.05
#         return interest
    
# acc1 = SavingsAccount("101", "Ansh", 100000)
# print("Balance : ", acc1.get_balance())
# print("Interest:", acc1.calculate_interest())

# QUES-2
from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self, account_number, name_holder, balance):
        self.__account_number = account_number
        self.__name_holder = name_holder
        self.__balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited : {amount}")
        else:
            print("Invalid amount")
        
    def withdrawl(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawl sucessfully")
        else:
            print("Insufficient amount")

    def get_balance(self):
        return self.__balance
    
    @abstractmethod
    def calculate_interest(self):
        pass


class SavingAccount(Account):
    interest_rate = 0.05
    def calculate_interest(self):
        interest = self.get_balance() *self.interest_rate
        print("Intrest is : ", interest)