# CONDITION SATEMENT
# how to input a value through user
# user_name = input("Enter your age : ")
# print("My age is : ", user_name)
# Ques-1 
# user_age = int(input("Enter your age :  \n"))
# if user_age < 13:
#     print("Child")
# elif user_age < 20:
#     print("Teenager")
# elif user_age < 60:
#     print("Adult")
# else:
#     print("Senior")
# Ques-2
# age = 15
# day = "Wednesday"
# price = 12 
# if age >= 18:
#     print(price)
# else:
#     print(price-4)
# if day == "Wednesday":
#     price -= 2
# print("Ticket price for you is $", price)
# Ques-3
# marks = 91
# if marks <= 100 & marks >= 90:
#     print("Grade A")
# elif marks <= 89 & marks >= 80:
#     print("Grade B")
# elif marks <= 79 & marks >= 70:
#     print("Grade C")
# elif marks <= 69 & marks >= 60:
#     print("Grade D")
# else:
#     print("Grade F")
# Ques-4
# fruit = input("Enter Fruit : ")
# color = input("Enter fruit color : ") 

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("Overripe")
# else:
#     print("Select correct fruit")
# Ques-5
# weather = input("Enter weather : ")
# if weather == "Sunny":
#     print("Go for walk")
# elif weather == "Rainy":
#     print("Read a book")
# elif weather == "Snowy":
#     print("Build a snowman")
# Ques-6
# distance = int(input("Enter your distance : \n"))
# if distance < 3:
#     print("Walk")
# elif distance <= 15:
#     print("Bike")
# elif distance > 15:
#     print("Car")
# Ques-7
# order = input("Enter your coffee size : ")
# coffee_shot = input("If you want add some other encridients : ").strip().lower()

# if coffee_shot == "true":
#     print(order + " Coffee with extra shots")
# else:
#     print(order + " Coffee")
# Ques-8
# pet = input("Enter your pet catagories : ")
# age = int(input("Enter your pet age : "))
# if pet == "Dog":
#     if age < 2:
#         print("Puppy Food")
#     elif age > 2:
#         print("Senior Dog Food")
# elif pet == "Cat":
#     if age > 5:
#         print("Senior cat food")
#     elif age < 5:
#         print("Junior cat food")
# Ques-9
# year = int(input("Enter year : "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("{} is a leap year".format(year))
# else:
#     print("{} is not a leap year".format(year))