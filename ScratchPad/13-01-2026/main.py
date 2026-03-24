# TUPLE
# QUES-1 EK TUPLE LOO OR ESMA SE SUM OF ELEMENTS FIND KARO LOOP SE
# my_tuple = (1, 2, 3, 4, 5)
# sum = 0
# for i in my_tuple:
#     sum += i
# print("The sum of the number is : ",sum)

# QUES-2 TUPLE KO LIST ME CONVERT KARO AUR USME ELEMENT ADD KRKE VAPAS SA TUPLE BANA DO
# t = (1, 2, 3, 4, 5)
# l = list(t)
# print(l)
# t = tuple(l)
# print(t)

# QUES-3 TUPLE UNPACKING EXAMPLE
# EXAMPLE - 1
# x = (1, 2, 3, 4, 5)
# a, b, *rest = x

# print(a)
# print(b)
# print(rest)

# QUES-4 TUPLE MA MINIMUM VAUE FIND KARO BINA min() KA 
# t = (90, 2, 3, 4, 5)
# smallest = len(t)-1
# for i in t:
#     if i < smallest:
#         smallest = i
# print(smallest)

# QUES-5 TUPLE KA HAR EK ELEMENT KA SQUARE PRINT KARO 
# t = (1, 2, 3, 4, 5)
# for i in t:
#     i= i ** 2
#     print(i, end=" ")

# DICTIONARY
# QUES-1 5 STUDENT KA NAME OR MARKS INPUT LEKE DICTIONARY BANAO
# d = {}
# n = int(input("How many entries that you filled: "))
# for i in range(n):
#     name = input("Enter the student name : ")
#     marks = input("Enter the marks : ")
#     d[name] = marks
# print(d)

# QUES-2 DICTIONARY MA SA HIGHEST NUMBER VALA STUDENT PRINT KARO
# student = {}
# n = int(input("Enter the how many entries that you have to enter that : "))
# for i in range(n):
#     name = input("Enter the student name: ")
#     marks = input("Enter the student marks: ")
#     student[name] = marks
# topper = max(student, key=student.get)
# print("\nAll Students : ", student)
# print("Topper : ", topper)
# print("Highest marks : ", student[topper])

# QUES-3 DICTIONARY KA SABHI VALUE KA AVERAGE NIKALO
# value = {}
# n = int(input("Enter the entries : "))
# for i in range(n):
#     key = input("Key : ")
#     value = input("Value: ")
#     value[key] = value

# total = sum(value.values())
# avg = total/len(value)

# QUES-4 DICTIONARY MA DUPLICATE VALUES KA COUNT NIKALO
# d = {
#     "Rahul": 80,
#     "Neha": 75,
#     "Aman": 80,
#     "Pooja": 90,
#     "Riya": 75}
# freq = {}   
# for value in d.values():
#     if value in freq:
#         freq[value] += 1
#     else:
#         freq[value] = 1
# duplicate = {}
# for k, v in freq.items():
#     if v > 1:
#         duplicate[k] = v
# print(duplicate)

 