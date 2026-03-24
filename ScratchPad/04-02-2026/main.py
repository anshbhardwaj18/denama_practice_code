# QUES-1
# def even_number_sum(n):
#     sum = 0
#     for i in range(n):
#         if i % 2 == 0:
#             sum = sum + i
#     return sum

# print(even_number_sum(1001))

# QUES-2
# s = input("Enter something : ")
# rev = ""
# i = len(s) - 1
# while i>=0:
#     rev = rev + s[i]
#     i -= 1
# print("Reversed String : ", rev)

# a = input("Enter someting : ")
# rev = ""
# for ch in a:
#     rev = ch + rev
# print("Rversed string : ", rev)


# QUES-3
# a = input("Enter something : ")
# count = 0
# for ch in a:
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
#         count += 1
# print("Number of vowels : ", count)


# QUES-4
# SPLIT STRING
s = input("Enter something : ")

word = []
temp = ""

for ch in s:
    if ch != " ":
        temp += ch
    else:
        word.append(temp)
        temp = ""
word.append(temp)

print("Word split : ", word)