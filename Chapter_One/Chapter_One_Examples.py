# name = input()
# age = int(input())
# if name == "Alice":
#     print("Hi, Alice.")
# elif age < 12:
#     print("You are not alice, Kiddo.")
# else:
#     print("You are neither Alice nor a little kid.")
#
# spam = 0
# if spam < 5:
#     print("Hello, world.")
#     spam = spam + 1
#
#
# spam = 0
# if spam < 5:
#     print("Hello, world.")
#     spam = spam + 1
#
#
# name = " "
# while name != "Okoroafor Kelechi Divine":
#     print("Please type your name.")
#     name = input()
# print("Thank you!")

#
# name = " "
# while True:
#     print("Please type your name.")
#     name = input()
#     if name == "okoroafor kelechi":
#         break
# print("Thank you!")

#
# while True:
#     print("Hello world!")
#     # This code wil be an infinte loop

# while True:
#     print("Hello world!")
#     break
#     # This code will surely break if the condition is true
#
#
# while True:
#     print("who are you?")
#     name = input()
#     if name != "joe":
#         continue
#     print("Hello, Joe. what is the password? (It is a fish.)")
#     password = input()
#     if password == "swordfish":
#         break
# print("Access granted.")
#
# total = 0
# for num in range(101):
#     total = total + num
# print(total)
#
# print("My name is: ")
# i = 0
# while i < 5:
#     print("Jimmy five times (" + str(i) + ")")
#     i = i + 1
#
# import random
# for i in range(1):
#     print(random.randint(1, 101))
#
# import sys
#
# while True:
#     print("Type exit to exit.")
#     response = input()
#     if response == "exit":
#         sys.exit()
#     print("You typed " + response + ".")
#
# spam = 0
# if spam == 10:
#     print("eggs")
#     if spam > 5:
#         print("bacon")
#     else:
#         print("ham")
#     print("spam")
# print("spam")
#
# def hello():
#     print("Howdy!")
#     print("Howdy!!!")
#     print("Hello there. ")
#
#
# hello()
# # hello()
# # hello()
#
# def hello(name):
#     print("Hello " + name)
#
#
# hello("Alice")
#
# import random
#
#
# def get_answer(answer_number):
#     if answer_number == 1:
#         return "It is certain"
#     elif answer_number == 2:
#         return "It is decidedly so"
#     elif answer_number == 3:
#         return "yes"
#     elif answer_number == 4:
#         return "reply lazy try again"
#     elif answer_number == 5:
#         return "ask again later"
#     elif answer_number == 6:
#         return "concentrate and ask again"
#     elif answer_number == 7:
#         return "my reply is no"
#     elif answer_number == 8:
#         return "outlook not so good"
#     elif answer_number == 9:
#         return "very doubtful"
#
#
# secure_random = random.randint(1, 9)
# fortune = get_answer(secure_random)
# print(fortune)
#
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)


# def bacon():
#     ham = 101
#     eggs = 0
#
#
# spam()
#
#
# def spam():
#     print(eggs)
#
#
# eggs = 42
# spam()
# print(eggs)

#
# def spam():
#     print(eggs)
#
#
# eggs = 42
# spam()
# print(eggs)
#
#
# def spam():
#     eggs = 'spam local'
#     print(eggs)
#
#
# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)
#
#
# eggs = 'global'
# bacon()
# print(eggs)
#
#
# def spam():
#     global eggs
#     eggs = 'spam'


# eggs = 'global'
# spam()
# print(eggs)

# def spam(divide_by):
#     return 42 / divide_by
#
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

#
# def spam(divide_by):
#     try:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         pass
#
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


# def spam(divideBy):
#     return 42 / divideBy
#
#
# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print('Error: Invalid argument.')

#
# def modify_week(parameter_week):
#     week_order = [1, 2, 3, 4, 5, 6, 0]
#     parameter_week = [parameter_week[order] for order in week_order]
#     return parameter_week
#
#
# my_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
#            'Thursday', 'Friday', 'Saturday']
#
# print(modify_week(my_week))
#
#
# def modify_week(weeks):
#     weeks.append(weeks.pop(0))
#     return weeks
#
#
# my_week.append("Sunday")
#
# tasks = ["Java", "Sleep", "Python",
#          "Data Science", "Catch Cruise", "Flex", "Flex"]
# my_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
#            'Thursday', 'Friday', 'Saturday']
#
# (zip(my_week, tasks))
#
#
# def make_daily_plans(days_of_week):
#     my_daily_plans = {}
#     for x, y in zip(my_week, tasks):
#         my_daily_plans[x] = y
# #         return my_daily_plans
#
#
# print(make_daily_plans(my_week))
# print(make_daily_plans(my_week))
# print(make_daily_plans(my_week))
# print(make_daily_plans(my_week))
# print(make_daily_plans(my_week))
# print(make_daily_plans(my_week))
# print(make_daily_plans(my_week))

# squares = ["One", "Two", "Three", "Four", "Five", "Six"]
# values = [1, 2, 3, 4, 5, 6]
#
#
# def change_value(squares, values):
#     my_value = {}
#     for x, y in zip(squares, values):
#         my_value[x] = y ** 2
#     return my_value
#
#
# print(change_value(squares, values))
#

# def lazy_range(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#         return i
#
#     for i in lazy_range(10):
#         pass
#     print(lazy_range(i))
#
# def natural_number():
#     n = 1
#     while True:
#         yield n
#         n += 1


# cat_names = []
# while True:
#     print("Enter the name of cat " + str(len(cat_names) + 1) +
#           ' (or enter nothing to stop.):')
#
#     name  = input()
#     if name == " ":
#         break
#     cat_names  = cat_names + [name]
# print("The cat names are : ")
# for name in cat_names:
#     print(' '  + name)
#

# supplies = ["pens", "staples", "flame-throwers", "binders"]
# for total_number  in range(len(supplies)):
#     print('index ' + str(total_number) + ' in supplies is: ' + supplies[total_number])

# my_pets = ["Zophie", "pooka", "fat-tail"]
# print("Enter a pet name: ")
# name = input()
# if name not in my_pets:
#     print(f"I don't have a pet named  {name}")
# else:
#     print(f"{name} is my pet.")

# cat = ['fat', 'black', 'loud']
# size, color, disposition = cat
# print(cat)

# spam = 'Hello'
# spam += ' World!'
# print(spam)
#
# spam = ['hello', 'hi', 'howdy', 'heyas']
# print(spam.index('hello'))

 # spam = ['cat', 'dog', 'bat']
# spam.append('moose')
# print(spam)

# spam = ['cat', 'dog', 'bat']
# spam.insert(1, 'chicken')
# print(spam)
#
# spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
# spam.remove('cat')
# print(spam)

# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# print(spam)
#
# import random
#
# messages = ['It is certain',
#             'It is decidedly so',
#             'Yes definetely',
#             'Ask again later',
#             'My reply is no',
#             'Outlook not so good',
#             'Very doubtful']
# print(messages[random.randint(0, len(messages) -1)])
#
# name = 'Zophie'
# print(name[0])
# print(name[-2])
# print(name[0:4])
# print('Zo' in name)
# for list in name:
#     print('* * * ' + list + ' * * *')

# spam = [0, 1, 2, 3, 4, 5]
# chess = spam
# chess[0] = 'New Variable'
# print(spam)


# def eggs(some_parameter):
#     some_parameter.append('Hello')
#
# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

# import copy
# spam = ['A', 'B', 'C', 'D']
# chesse = copy.copy(spam)
# chesse[1] = 42
# print(chesse)
# print(spam)
