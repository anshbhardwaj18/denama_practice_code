# name = input("Enter you name : ")
# age = int(input("How old are you {} : ".format(name)))

# print("Your age is : ", age)

# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Come back in {} year".format(18-age))

name = input("Enter your name :  \n")
age = int(input("Enter your age : "))

if age >= 18 and age < 31:
    print("Holiday")
else:
    print("You are teenager so, you don't have holiday")