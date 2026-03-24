# *************************************LIST***************************************
# QUES-1
# EK LIST LOO JISME RANDOM NUMBERS HO. Even number left, Odd number right shift karo
# def nums(l1):
#     even = []
#     odd = []
#     for i in l1:
#         if i == 0:
#             continue
#         elif i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     result = even + odd
#     print(result)
# nums([0, 2, 7, 9, 3, 6, 8, 10])

# QUES-2
# Bina inbuilt function use kiye second largest element nikalo.
# def num2(nums):

#     largest = nums[0]
#     second_largest = -1

#     for i in nums:
#         if i > largest:
#             second_largest = largest
#             largest = i
#         elif i < largest and i > second_largest:
#             second_largest = i

#     print(second_largest)

# num2([90, 45, 87, 32, 88])

# QUES-3
# Ek list ko rotate karo k steps right.

# l1 = [10, 50, 30, 20, 40]
# k = 2
# n = len(l1)
# k = k % n

# for i in range(k):
#     last = l1[-1]
#     j = n - 1
#     while j > 0:
#         l1[j] = l1[j - 1]
#         j -= 1
#     l1[0] = last
# print(l1)

# QUES-4 
# Do list lo → common elements nikalo (duplicates nahi).
# l1 = [10, 20, 30, 40, 50]
# l2 = [20, 30, 40, 50, 60]
# common = []
# for i in l1:
#     if i in l2 and i not in common:
#         common.append(i)
# print(common)

# QUES-5
# Ek list me har element ka frequency count banao (dictionary use kiye bina).
# l1 = [10, 60, 40, 10, 20, 40]
# l2 = []
# for i in l1:
#     if i in l2:
#         continue
#     count = 0
#     for j in l1:
#         if i == j:
#             count += 1
#     l2.append(i)
#     print(i, "->", count)
# ***************************************Dictionary ka sath************>>>>>>>>>>>>>>
# l1 = [10, 60, 40, 10, 20, 40]
# freq = {}
# for i in l1:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)
# **************************************TUPLE*************************************
# n = 5
# f = 1
# for i in range(1, n+1):
#     f = f * i
# print(f)

# def nums(lst):
#     sum = 1
#     for i in lst:
#         sum = sum * i
#     print(sum)
# nums([1, 2, 3, 4]) 

# a = [1, 2, 1]
# if a == a[::-1]:
#     print("palindrome")
# else:
#     print("is not palindrome") 
# import tkinter as tk

# root = tk.Tk()          # window create
# root.title("My First GUI")
# root.geometry("300x200")

# label = tk.Label(root, text="Hello Bhai 😄")
# label.pack()

# root.mainloop()

# def click_me():
#     print("Button dabaya bhai 😎")

# btn = tk.Button(root, text="Click Me", command=click_me)
# btn.pack()

import turtle

t = turtle.Turtle()   # turtle create
# t.forward(100)        # aage jao 100 steps
# t.left(90)            # left ghoomo
# t.forward(100)

# turtle.done()
# t = turtle.Turtle()

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# turtle.done()
# t.color("blue")

# for i in range(5):
#     t.forward(100)
#     t.right(144)

# turtle.done()


def split_string(s):
    mid = len(s) // 2

    str2 = s[:mid]
    str3 = s[mid:]

    return str2, str3

s = "PS C:\\Denama\\Learning\\PythonPractice> & C:/Program Files/Python312/python.exe c:/Denama/Learning/PythonPractice/dnm_audit.py"

str2, str3 = split_string(s)
print("Right : ", str2)
print("Left : ", str3)