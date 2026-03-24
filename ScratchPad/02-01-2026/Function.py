# QUES-1 FUNCTION SYNTAX:
# WRITE A FUNCTION TO CALCULATE THE SQAURE OF A NUMBER
# def square(number):
#     return number ** 2
# result = square(4)
# print(result)
# ***************************************************************
# QUES-2 FUNCTION WITH MULTIPLE PARAMETER
# CREATE A FUNCTION THAT TAKES A TWO NUMBERS AS PARAMETERS AND RETURN THEIR VALUES.
# def sum(numOne, numTwo):
#     return numOne + numTwo
# print(sum(4, 5))
# ***************************************************************
# QUES-3 POLYMORPHISM IN FUNCTION
# WRITE A FUNCTION MULTIPLY THAT MULTIPLIES TWO NUMBERS, BUT CAN ALSO ACCEPT AND MULTIPLY STRINGS.
# def multiply(p1, p2):
#     return p1**p2
# print(multiply(2, 3))
# ***************************************************************
# QUES-4 FUNCTION RETURN MULTIPLE VALUE
# CREATE A FUNCTION THAT RETURNS BOTH THE AREA AND CIRCUMFRENCES OF A CIRCLE GIVEN ITS RADIUS,
# import math
# def circule_stats(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference
# a, c = circule_stats(3)
# print("1) Area: ", a , "\n2) circumference: ", c)
# ***************************************************************
# QUES-5 Default Parameter Value
# Write a function that greet a user. If no name is provide, it should greet with a default name.
# def greet(name= "User"):
#     return "Hello " + name + " !"
# print(greet("Ansh"))
# print(greet())
# QUES-6 LAMBDA FUNCTION
# CREATE A LAMBDA FUNCTION TO COMPUTE THE CUBE OF A NUMBER.
# cube = lambda x : x ** 3
# print(cube(3))

# ***************** 06-01-2026 ******************
# QUES-7 FUNCTION WITH *ARGS
# Write a function that takes variable numbers of arguments and return their sum.
# def sum_all(*ansh):
#     print(*ansh)
#     for i in ansh:
#         print(i * 2)
#     return sum(ansh)
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# QUES-8 FUNCTION WITH **KWARGS
# CREATE A FUNCTION THAT ACCEPTS ANY NUMBERS OF KEYWORD ARGUMENTS AND PRINTS THEM IN THE FORMAT KEY: VALUE.
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_kwargs(name="shaktiman", power="lazer")

# QUES-9 GENERATOR FUNCTION WITH FIELD
# WRITE A GENERATOR FUNCTION THAT YIELDS EVEN NUMBERS UP TO A SPECIFIED LIMIT.
# def even_number(limits):
#     for i in range(2, limits+1, 2):
#         yield i

# for num in even_number(10):
#     print(num)
# ***************************************
# def test():
#     print("Start")
#     yield 1
#     print("Middle")
#     yield 2
#     print("End")
# g = test()
# print(next(g))
# print(next(g))
# ************************************************************************
# QUES-10 RECURSIVE FUNCTION
# CREATE A RECURSIVE FUNCTION TO CALCULATE THE FACTORIAL OF A NUMBER.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))