# STRING IN PYTHON
# Ques 1 : How to initialize a String:-
# name = "Ansh"
# city = "Ghaziabad"
# msg = "Python is awesome"
# print(name)
# print(city) 
# print(msg)

# Ques 2 : String important operator
# 1. Length nikalna. [syntax = len()]
# text = "Here i am writing a python code"
# print(len(text))

# 2. Indiexing position sa letter nikalna
# word = "Python"
# print(word[0])

# 3. Slicing (String ka part nikalna)
# word = "programming"
# print(word[0:5])
# print(word[3:7])

# 4. String ko join karna(Concatination)
# first = "Ansh"
# last = "bhardwaj"
# print(first + " " + last)

# USEFUL STRING FUNCTION
# text = "Python programming"

# jab huma sare word ya letter capital ma krne hoo:-
# print(text.upper())
# jab huma sare word ya letter smaller ma krne hoo:-
# print(text.lower())
# jab huma first word ka first letter capital ma krna hoo:-
# print(text.capitalize())
# jab huma kisi word ko replace krke kuch or word likhna hoo:-
# print(text.replace("Python", "Java"))

#  check krna ki voo word joo hum check krna cahate ha ki voo uss string ma ha ya nhi
# msg = "I Love Python"
# print("Python" in msg)

# String immutable hoti hai // true
# matlab ki string change nhi hoti
# name = "Ansh"
# name = "B" + name[1:]
# print(name)

# Split() - String ko todna
# line = "I Love Python"
# print(line.split())

# Join() - List ko String banana
# word = ["I", "Love", "Python"]
# print(" ".join(word))

# Strip(), lstrip(), rstrip()
# msg = "  hello  "
# print(msg.strip())
# print(msg.lstrip())
# print(msg.rstrip())

# find() vs index()
# text = "Python"
# print(text.find("P"))

# count()
# text = "banana"
# print(text.count("a"))

# startswith()/endswith()
# email = "ansh457@gmail.com"
# print(email.startswith("@gmail.com"))
# print(email.endswith("ansh457"))

# String formatting(Interview perspective)
# name = "Ansh"
# age = 21
# answer = "My name is {} and my age is {}"
# print(answer.format(name, age))

# Reverse String
# text = "Python"
# print(text[::-1])

# ESCAPE CHARACTER
# text = "My name is\nAnsh"
# print(text)

# buns = 2.40
# customer_money = 15
# print(customer_money // buns)

# meal1 = "spam" + "eggs" + "beans"
# meal2 = "spam\neggs\nbeans"
# meal3 = "spam, eggs, beans"
# meal4 = """spam
# eggs
# beans"""
# print(meal1)
# print(meal2)
# print(meal3)
# print(meal4)

# a = 45
# b = 15
# c = 3

# print(a-b/c)

# quantity = 10
# price = 5.0
# total = quantity * price
# tax = total/5

# Total = total + tax
# print(Total)


# days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
# print(days[::5])

# data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

# print(data[::5])
# print(data[1:5])
# print(data[0:-1:5])
# print(data[:-1:5])