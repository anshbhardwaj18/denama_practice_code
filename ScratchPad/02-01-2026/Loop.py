# LOOPS IN PYTHON
# ************************************************************************
# QUES-1 COUTNING A NUMBER:
# GIVEN A LIST OF NUMBERS, COUNT HOW MANY NUMBERS ARE NEGATIVE.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
# print("Final positive number count is : ", positive_number_count)
# ************************************************************************
# QUES-2 SUM OF EVEN NUMBER:
# CALCULATE THE SUM OF EVEN NUMBER UP TO A GIVEN NUMBER N.
# n = int(input("Enter the number : "))
# sum_even = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print("The even number is : ", i)
#         sum_even += i
# print("Sum of even number is : ", sum_even)
# ************************************************************************
# QUES-3 PRINT THE TABLE:
# PRINT THE MULTIPLICATION TABLE FOR A GIVEN NUMBER UP TO 10, BUT SKIP THE FIFTH ITERATION.
# number = int(input("Enter the number : \n"))
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, 'x' , i, '=', number * i)
# ************************************************************************
# QUES-4 REVERSE A STRING:
# REVERSE A STRING USING A LOOP
# input_str = input("Enter you string :  ")
# reversed_str = ""
# for char in input_str:
#     reversed_str = char + reversed_str
# print(reversed_str)'
# ************************************************************************
# QUES-5 FIND THE FIRST NON-REPEATED CHARACTER:
# GIVEN A STRING, FIND THE FIRST NON-REPEATED CHARACTER
# input_str = input("Enter String : ")
# for char in input_str:
#     if input_str.count(char) == 1:
#         print("Char is : ",char)
# ************************************************************************
# QUES-6 FACTORIAL OF A NUMBER:
# COMPUTE THE FACTORIAL OF A NUMBER USING A WHILE LOOP
# number = int(input("Enter the number : \n"))
# fact = int(input("Enter the end number : \n"))
# while number > 0:
#     fact *= number
#     number -= 1
# print("The factorial of number is : ", fact)
# ************************************************************************
# QUES-7 VALIDATe INPUT:
# KEEP ASKING THE USER FOR INPUT UNIT THEY ENTER A NUMBER BETWEEN 1 AND 10.
# while True:
#     number = int(input("Enter a number between 1 and 10 : "))
#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Re-Enter a valid number")
# ************************************************************************
# QUES-8 PRIME NUMBER CHECKER:
# CHECK IF A NUMBER IS PRIME OR NOT
# number = int(input("Enter a number : "))
# is_prime = True
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break
# print("Is a prime number or not : ", is_prime)
# ************************************************************************
# QUES.9 LIST UNIQUENESS CHECKER
# CHECK IF ALL THE ELEMENT IN LIST ARE UNIQUE. IF A DUPLICATE IS FOUND, EXIT THE LOOP AND PRINT THE DUPLICATE
# items = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print("Duplicate : ", item)
#         break
#     unique_item.add(item)
# ************************************************************************
# QUES.10 EXPONENTIAL NUMBER
# IMPLEMENT AN EXPONENTIAL BACKOFF STRATEGY THAT DOUBLES THE WAIT TIME BETWEEN RETRIES, STARTING FROM 1 SECOND, BUT STOP AFTER 5 RETRIES.
# import time

# wait_timer = 1
# attempts = 0
# max_retries = 5

# while attempts < max_retries:
#     print("Attempts", attempts + 1, "-wait timer", wait_timer)
#     time.sleep(wait_timer)
#     wait_timer *= 2
#     attempts += 1