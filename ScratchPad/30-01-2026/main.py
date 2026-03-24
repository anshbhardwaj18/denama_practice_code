# PRACTISE QUESTION OF PYTHON.
# *****************LIST****************
# QUES-1
# lst = [1, 3, 5, 7, 2, 4, 6, 8, 0]
# even = []
# odd = []
# for i in lst:
#     if i == 0:
#         continue
#     elif i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# result = even + odd
# print(result)

# QUES-2
# lst = [1, 1, 1, 1, 1, 1, 1]
# largest = lst[0]
# second_largest = -1

# for i in lst:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i < largest and i > second_largest:
#         second_largest = i
# if second_largest == -1:
#     print("All the numbers are same there are no element of second largest number")
# else:
#     print("Second largest : ", second_largest)

# QUES-3
# lst = [1, 2, 3, 4, 5]
# k = 3
# n = len(lst)
# k = k % n

# for i in range(k):
#     last = lst[-1]
#     j = n - 1
#     while j > 0:
#         lst[j] = lst[j-1]
#         j -= 1
#     lst[0] = last

# print(lst)

# QUES-4 
# lst1 = [10, 20, 30, 40, 50]
# lst2 = [20, 30, 40, 50, 60]

# common = []

# for i in lst1:
#     if i in lst2 and i not in common:
#         common.append(i)
# print(common)

# QUES-5
# lst = [10, 20, 30, 10, 30, 40]
# freq = []
# for i in lst:
#     if i in freq:
#         continue
#     count = 0
#     for j in lst:
#        if i == j:
#           count += 1
#     freq.append(i)
#     print(i, "->", count)

# QUES-6
# lst = [1, 2, 3, 4, 5]
# sum = 0
# for i in lst:
#     sum = sum + i
# print(sum)

# QUES-7
# lst = [1, 2, 3, 4, 5]
# mul = 1
# for i in lst:
#     mul = mul * i
# print(mul)

# QUES-8
# lst = [1, 2, 3, 4, 5]
# sum = 0
# for i in lst:
#     sum = sum + i
#     avg = sum/5
# print(avg)

# QUES-9
# lst = [1, 2, 3, 4, 5]
# rev = lst[::-1]
# print(rev)


# ************************* TUPLE ************************
# QUES-1    
# tu = (1, 2, 3, 4, 5)
# update = list(tu)
# print(update)
# re_update = tuple(tu)
# print(re_update)

# QUES-2
# tup = ("ansh", "bhardwaj", "javascript", "python")
# max_str = ""
# max_len = 0
# for i in tup:
#     length = 0
#     for ch in i:
#         length += 1
    
#     if length > max_len:
#         max_len = length
#         max_str = i
# print(max_str)

# QUES-3
# def sum_numbers_manual(tup):
#     total = 0
#     for elem in tup:
#         try:
            # agar number hai toh add
        #     total += elem
        # except TypeError:
            # agar TypeError aaya matlab tuple ya non-number
            # fir recursion call karo
    #         total += sum_numbers_manual(elem)
    # return total

# Example
# tup = (1, 2, ("a", 3, 4), (5, "b", (6, 7)))
# print("Sum of numbers:", sum_numbers_manual(tup))


# def sum_numbers(tup):
#     total = 0
#     for elem in tup:
#         if isinstance(elem, (int, float)):  
#             total += elem
#         elif isinstance(elem, tuple):       
#             total += sum_numbers(elem)      
#     return total
# tup = (1, 2, ("a", 3, 4), (5, "b", (6, 7)))
# print("Sum of numbers:", sum_numbers(tup))


# QUES-4
# tup = (1, 2, 3, 4, 5)
# rev = tup[::-1]
# print(rev)

# WITHOUT SLICING
# tup = (1, 2, 3, 4, 5)

# rev = ()
# i = len(tup) - 1

# while i >= 0:
#     rev = rev + (tup[i],)
#     i -= 1
# print(rev)

# QUES-5
# tup = (1, 2, 3, 5, 5)
# dup = ()
# for i in tup:
#     found = False
#     for x in dup:
#         if x == i:
#             found = True
#             break
#     if not found:
#         dup = dup + (i,)
# print(dup)

# ************************** SET *************************
# QUES-1
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# common = set()
# only_set1 = set()
# only_set2 = set()
# for i in set1:
#     if i in set2:
#         common.add(i)
#     else:
#         only_set1.add(i)
# for y in set2:
#     if y not in set1:
#         only_set2.add(y)
# print("only_set1 : ", only_set1)
# print("common : ", common)
# print("only_set2 : ", only_set2)

# QUES-2
# lst = [1, 2, 3, 1, 2, 3]
# result = set(lst)
# print(result)

# QUES-3
# set1 = {1, 2, 3, 4, 5}
# new_set = set()
# for i in set1:
#     if i % 2 != 0:
#         new_set.add(i)
# print(new_set)

# QUES-4
# set1 = {1, 2}
# set2 = {1, 2, 3, 4, 5}
# is_subset = True
# for i in set1:
#     found = False
#     for y in set2:
#         if i == y:
#             found = True
#             break
#     if not found:
#         is_subset = False
#         break
# if is_subset:
#     print("Set 1 is subset of Set2")
# else:
#     print("Set 1 is not subset of Set2")


# set1 = {1, 2}
# set2 = {1, 2, 3, 4, 5}
# is_subset = True
# for i in set1:
#     if i not in set2:
#         is_subset = False
#         break
# if is_subset:
#     print("Set 1 is subset of set2")
# else:
#     print("Set 1 is not subset of set 2")

# ***************************** OOPS ******************************
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def calculate_marks(self):
        if self.marks >= 80:
            print("Grade : A")
        elif self.marks >= 60:
            print("Grade : B")
        elif self.marks >= 40:
            print("Grade : C")
        else:
            print("Grade : Fale")

s1 = Student("Ansh", 75)
print(s1.name)
print(s1.marks)