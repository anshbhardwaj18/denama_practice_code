# PRACTISE OF PREVIOUS CONCEPTS OF PYTHON
# TUPLE
# name = ("ansh", "akshit", "pushkar", "sparsh", "dev")
# name = ("maanu", "aashu", "pussu", "tapu", "dkboss")
# print(name)
# 
# LIST
# Ques-1 USER SE 8 NUMBER LOO AUR:
# EVEN NUMBER EK LIST ME
# ODD NUMBER EK LIST ME
# list1 = []
# print("Enter 8 numbers: ")
# for i in range(8):
#     num = int(input())
#     list1.append(num)
# even = []
# odd = []
# for i in list1:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even numbers are: ", even)
# print("odd numbers are: ", odd)

# QUES-2 USER SE NUMBER LO KUCH OR VAHI NUMBER PRINT KARAO JOO 15 SA BADA HO
# list2 = []
# n = int(input("Enter the range: "))
# print("Enter the number: ")
# for i in range(n):
#     num = int(input())
#     list2.append(num)

# bigger_than_15 = []
# for i in list2:
#     if i > 15:
#         bigger_than_15.append(i)
# print("Numbers greater than 15 are: ", bigger_than_15)  

#QUES-3 EK LIST ME SE SECOND LARGEST NUMBER FIND KARO
# list3 = []
# n = int(input("Enter the range : "))
# print("Enter the numbers: ")
# for i in range(n):
#     num = int(input())
#     list3.append(num)

# largest = list3[0]
# smallest = list3[0]

# for i in list3:
#     if i > largest:
#         smallest = largest
#         largest = i
#     elif i > smallest and i != largest:
#         smallest = i
# print("The second largest number is: ", smallest)

# QUES-4 EK LIST KO REVERSE KARO BINA REVERSE FUNCTION KE OR SLICING KE
# list4 = []
# n = int(input("Enter the range: "))
# print("Enter the numbers: ")
# for i in range(n):
#     num =int(input())
#     list4.append(num)
# reversed_list = []
# for i in range(len(list4)-1, -1, -1):
#     reversed_list.append(list4[i])
# print("Reversed list is: ", reversed_list)
# **************** DUSRA TARIKA ******************
# list4 = []
# n = int(input("Enter the range: "))
# print("Enter the numbers: ")
# for i in range(n):
#     num = int(input())
#     list4.append(num)
# start = 0
# end = len(list4) - 1
# while start < end:
#     list4[start], list4[end] = list4[end], list[start]
#     start += 1
#     end -= 1
# print("Reversed list is: ", list4)