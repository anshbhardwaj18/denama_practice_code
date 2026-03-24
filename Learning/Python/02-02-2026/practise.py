# QUES-1 Make a calculator 
# This is only simple calculator only 1 operation at one time
# def calculator():
#     a = int(input("Enter your 1st number : "))
#     b = int(input("Enter your 2nd number : "))

#     result = a + b

#     return result
# answer = calculator()
# print("Your answer is : ",answer)

# This is a 2nd code of question 1st to perform all operation
# def calculator(num1, num2, op):
#     if op == '+':
#         return num1 + num2
#     elif op == '-':
#         return num1 - num2
#     elif op == '*':
#         return num1 * num2
#     elif op == '/':
#         if num2 == 0:
#             return "Please enter valid input"
#         return num1 / num2
#     else:
#         "Invalid operation"
    
# while True:
#     try:
#         num1 = float(input("Enter your 1st number : "))
#         num2 = float(input("Enter your 2nd number : "))
#         op = input("Enter your operation that you are perform with number(+, -, *, /) : ")

#         result = calculator(num1, num2, op)
#         print(result)
#     except:
#         print("Invalid input please check and reenter the value : ")

#     choice = input("Do you want to continue calculation(yes/no) : ")
#     if choice != "yes":
#         print("Calculation stop!.")
#         break

# QUES-2 Student result analyzer
# marks = []
# n = int(input("Enter the range : "))
# for i in range(n):
#     m = float(input("Enter student marks : "))
#     marks.append(m)
# avg = sum(marks) / len(marks)
# print("Average marks : ", avg)
# topper = max(marks)
# print("Topper student : ", topper)
# fail = []
# for m in marks:
#     if m < 40:
#         fail.append(m)
# print("Fail student marks : ", fail)
# print("\nGrade : ")
# for m in marks:
#     if m >= 90 and m <= 100:
#         grade = 'A'
#     elif m >= 75 and m <= 89:
#         grade = 'B'
#     elif m >= 50 and m < 75:
#         grade = 'C'
#     elif m >= 40 and m <50:
#         grade = 'D'
#     else:
#         grade = 'Fail' 
#     print(m , " -> ", grade)

# QUES-3 Password Validator"
# def validator(str):
#     if len(str) < 8:
#         return False
#     has_digit = False
#     has_special = False
#     has_upper = False
#     for ch in str:
#         if ch.isdigit():
#             has_digit = True
#         elif ch.isupper():
#             has_upper = True
#         elif not ch.isalnum():
#             has_special = True       
#     return has_digit and has_upper and has_special
# password = input("Enter your password : ")
# if validator(password):
#     print("Valid password")
# else:
#     print("Invalid Password")