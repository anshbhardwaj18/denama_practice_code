# LIST
# QUES-1 
# ---->>
# a = [1,2,3,5]
# a[3] = 4
# print(a)

# QUES-2
# ---->>
# a = [1,2,3,4]
# print(a.remove(2))
# print(a.pop())
# del a[0]

# QUES-3
# ----->>
# list = [1, 2, 3, 90, 5]
# first_largest = list[0]
# second_largest = None

# for i in list:
#     if i >= first_largest:
#         second_largest = first_largest
#         first_largest = i
#     elif i <= first_largest and i != second_largest:
#         second_largest = i
# print(first_largest)
# print(second_largest)

# FUNCTION------->>>>
# QUES-1 
# ---->>>
# def add(a, b):
#     return a + b
# print(add(3, 4))

# QUES-2
# ---->>>
# def greet(name = "user"):
#     return ("Hello", name)
# print(greet())

# QUES-3
# ---->>>
# def mul(a, b):
#     return a+b, a-b, a*b
# x, y, z= mul(10, 5)
# print(x, y, z)