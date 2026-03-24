# QUES-4
# INVENTORY MANAGEMENT:-
# inventory = {}

# while True:
#     print("\n---Inventory Management--->>>")
#     print("1. Add/Update Product")
#     print("2. Delete Product")
#     print("3. Search Product")
#     print("4. Total item count")
#     print("5. Show inventory")
#     print("6. Exit")

#     choice = input("Enter your choice : ")

#     if choice == '1':
#         name = input("Enter your product name : ").lower()
#         quanity = int(input("Enter product quantity : "))
#         inventory[name] = inventory.get(name, 0)+quanity
#         print("Product Update!")
    
#     elif choice == '2':
#         name = input("Enter your prdouct name you want to delete : ").lower()
#         if name in inventory:
#             del inventory[name]
#             print("Delete Sucessfully")
#         else:
#             print("Product not found")
    
#     elif choice == '3':
#         name = input("Enter you product name that you want to search : ").lower()
#         if name in inventory:
#             print(f"{name} -> quantity : {inventory[name]}")
#         else:
#             print("Product not found!")
        
#     elif choice == '4':
#         total = sum(inventory.values())
#         print("Total count of item : ", total)

#     elif choice == '5':
#         print("Inventory : ", inventory)
    
#     elif choice == '6':
#         print("Exiting program")
#         break
    
#     else:
#         print("Invalid input")

# QUES-5
# FILE LOGGER SYSTEM
# from datetime import datetime

# filename = "user_log.txt"

# while True:
#     print("\n---File logger system---")
#     print("1. Add user log")
#     print("2. Show logs")
#     print("3. Exit")

#     choice = input("Enter choice : ")

#     if choice == '1':
#         name = input("Enter your name : ")

#         time_now = datetime.now().strftime("%Y-%M-%D %H:%M:%S")

#         with open(filename, 'a') as file:
#             file.write(f"{time_now} - {name}\n")

#         print("Log saved!")

#     elif choice == '2':
#         print("\n---- Logs ----")

#         try:
#             with open(filename, 'r')as file:
#                 data = file.read()
#                 print(data if data else "No logs yet.")
#         except FileNotFoundError:
#             print("File not found!")

#     elif choice == '3':
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice!")

# from datetime import datetime

# filename = "user_log.txt"

# while True:
#     print("\n----- File Logger System -----")
#     print("1. Add user in file")
#     print("2. shows logs")
#     print("3. Exit")

#     choice = input("Enter your choice : ")

#     if choice == '1':
#         name = input("Enter your name : ")

#         time_now = datetime.now().strftime("%Y-%M-%D %H:%M:%S")

#         with open(filename, 'a') as file:
#             file.write(f"{time_now} - {name}\n")

#         print("Log Saved!")

#     elif choice == '2':
#         print("\n---- Logs ----")
#         try:
#             with open(filename, 'r') as file:
#                 data = file.read()
#                 print(data if data else "No logs yet!")
#         except FileNotFoundError:
#             print("File not found!")

#     elif choice == '3':
#         print("Exiting...")
#         break

#     else:
#         print("Invalid input")

# QUES-6 
# Bank Account
# class BankAccount():

#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#         self.deposit(balance)

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid deposit")
#         else:
#             self.__balance += amount
#             print(f"Deposited : {amount}")
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid amount withdraw")
#         elif amount > self.__balance:
#             print("Balance is not insufficient")
#         else:
#             self.__balance -= amount
#             print(f"Withdraw : {amount}")
    
#     def check_balance(self):
#         print(f"Account Holder : {self.name}")
#         print(f"Balance : {self.__balance}")

# acc = BankAccount("Ansh", 1000)
# acc.withdraw(300)
# acc.check_balance() 

# QUES-7
# EMPLOYEE -> MANAGER 
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     def show_employee(self):
#         print(f"Name : {self.name}")
#         print(f"Salary : {self.salary}")

# class Manager(Employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus

#     def total_salary(self):
#         total = self.salary + self.bonus
#         print(f"Total Salary (with bonus):  {total}")

# m = Manager("Ansh", 50000, 20000)
# m.show_employee()
# m.total_salary()

# QUES-8
# DATA CLEANER
# data = [10, "hi", 25, -3, "python", 40]
# clean = []

# for item in data:
#     if isinstance(item, int)and item > 0:
#         clean.append(item ** 2)
# print(clean)

# QUES-9
# Generator system
# def even_generator():
#     for i in range(1, 100):
#         if i % 2 == 0:
#             yield i
# total = 0

# for num in even_generator():
#     print(num, end= " ")
#     total += num
# print("\nSum:", total)


# QUES-10
# Mini Student Database
# import json

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def grade(self):
#         if self.marks >= 90:
#             return 'A'
#         elif self.marks >= 75:
#             return 'B'
#         elif self.marks >=50:
#             return 'C'
#         else:
#             return "Fail"
    
#     def to_dict(self):
#         return {"name" : self.name, "marks" : self.marks}

# students = []
# file_name = "students.json"


# def save_to_file():
#     data = [s.to_dict() for s in students]
#     with open(file_name, "w") as f:
#         json.dump(data, f)


# def file_to_load():
#     global students
#     try:
#         with open(file_name, "r")as f:
#             data = json.load(f)
#             students = [students(d["name"], d["marks"]) for d in data]
#     except:
#         students = []

# def add_student():
#     name = input("Enter your name : ")
#     marks = int(input("Enter your marks : "))
#     students.append(Student(name, marks))
#     save_to_file()
#     print("Student added!")

# def search_student():
#     name = input("Search student : ")
#     for s in students:
#         if s.name.lower() == name.lower():
#             print(s.name, s.marks, "Grade : ", s.grade())
#             return
#     print("Not Found!")

# def average_marks():
#     if not students:
#         print("No data!")
#         return
#     avg = sum(s.marks for s in students) / len(students)
#     print("Average marks : ", avg)

# def topper():
#     if not students:
#         print("No data!")
#         return
#     top = max(students, key=lambda s : s.marks)
#     print("Topper : ", top.name, top.marks)

# def show_all():
#     for s in students:
#         print("Name : ", s.name, "Marks : ", s.marks, "Grade: ", s.grade())

# file_to_load()

# while True:
#     print("\n--------- Student Database-------")
#     print("1. Add Student")
#     print("2. Show all")
#     print("3. Search")
#     print("4. Average")
#     print("5. Topper")
#     print("6. Exit")

#     ch = input("choice : ")

#     if ch == '1':
#         add_student()
#     elif ch == '2':
#         show_all()
#     elif ch == '3':
#         search_student()
#     elif ch == '4':
#         average_marks()
#     elif ch == '5':
#         topper()
#     elif ch == '6':
#         print("Exit...")
#         break
#     else:
#         print("Invalid input")