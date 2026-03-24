from functools import reduce
# def dictionary(dict):
#     return dict
# print({"name" : "ansh"})

# def dictionary():
#     dic = {}
#     for i in range(3):
#         user = input("Enter : ")
#         name = input("Enter your name : ")
#         dic[user] = name
#     return dic

# student_name = dictionary()
# print(student_name)

# def dictionary():
#     null_d = {}
#     user_input = int(input("Enter how many elements"))
#     for i in range(user_input):
#         key = input("Enter key")
#         value = input("ENter value")
#         null_d[key] = value
#         return null_d
# print(dictionary())

# def input_dictionary():
#     n = int(input("Kitne students ka data chahiye: "))
#     data = {}
#     for i in range(n):
#         name = input("Student name: ")
#         marks = int(input("Marks: "))
#         data[name] = marks
#     return data   
# print(input_dictionary())

# def list():
#     n = int(input("Enter your range : "))
#     l1 = []
#     for i in range(n):
#         user = int(input("Enter your list : "))
#         l1.append(user)
#     return l1
# print(list())

# def list(l1):
#     l2 = []
#     for i in l1:
#         l2.append(i)
#     return l2
# print(list([1, 2, 3]))

# def test():
#     print("Start")
#     return 1
#     # print("Middle")
#     # return 2
#     # print("End")

# print(test())

# def using_return():
#     return [i for i in range(100000000)]
# def using_yield():
#     for i in range(100000000):
#         yield i

# # lst = using_return()
# # print(lst)
# gen = using_yield()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# NORMAL FUNCTION
# def number(x):
#     return x*2
# print(number(5))

# LAMBDA FUNCTION
# def num():
#     n = int(input("Enter your range : "))
#     lst2 = []

#     for i in range(n):
#         user = int(input("Enter your list : "))
#         lst2.append(user)
#     return lst2

# even = list(filter(lambda x : x % 2 == 0, num()))
# print(even)

# def num():
#     n = int(input("Enter you range : "))
#     lst2 = []

#     for i in range(n):
#         user = int(input("Enter your list : "))
#         lst2.append(user)
#     return lst2

# odd = list(filter(lambda x : x % 2 != 0, num()))
# print(odd)



list1 = [1 , 2 , 3]
a = reduce(lambda x , y : x + y , list1)
print(a)