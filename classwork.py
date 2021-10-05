# scolarship percentage calculator
# for i in range(40, 101):
#   score = 50000 - (50000 * (i/100))
#   print(str(i)+"% = "+ str(score))
  
# this is to print a message on the screan
# print("robot is not hard it just need some level of intelligent and patience") # this is to print a message on the crean

"""
this is the first class of python 
we are good to go for robotic class
this program runs for couple of months
and we will surely succeed in it
"""

# Variables Declaration
# studentName = "Yemi"
# location = "General area"
# score = 70
# print("My name is "+studentName + " i stay in "+location +" and my total score is "+str(score) +" in Mathematics")

# firstName = input("please enter your name ")
# val1 = float(input("Enter first value "))
# val2 = float(input("Enter second value "))
# score = val1 + val2
# print("Welcome " + firstName + " your total score is "+ str(score))

# Global and Local variables
# a = 20

# def addition():
#     global a
#     b = 10
#     a = 30
#     score = a + b
#     print("Addition is ",score)

# def subtract():
#     b = 10
#     score = a - b
#     print("Subtraction is ",score)

# addition()
# subtract()

# Types of Datatype
# 1. Text types: String (str)
# 2. Numeric types: integer(int), float, complex
# 3. Sequence types: list, tuple, range
# 4. Mapping types: dictionary(dict)
# 5. Set types: set, frozenset
# 6. Boolean types: bool (True, False)
# 7. Binary types: bytes, bytearray, memoryview

# Examples
# string (str) example: "Johnson", "False", "56", '5.9ft', "this is my first python class"
# integer (int) example: 65, 80,
# float example: 7.8, 5.5, 0.3
# list example: [1,2,3,4,"one","two"]
# tuple example: (5,55,7,)
# range example: range(10)
# dictionary example: {"school":"SQI", "course":"Python"}
# set example: {1,2,3,4,5,6}
# frozenset example: ({1,2,3,4,5,6})
# bool example: True, False
# bytes example: b"Hello"

# Datatypes conversion
# To check for datatypes use type() function
# name = "45"
# print(type(name))
# str() to convert to string type 
# print("Type before convertion ", type(name))
# print("Type after convertion ", type(str(name)))
# int() to convert to integer type
# print("Type before convertion ", type(name))
# print("Type after convertion ", type(int(name)))
# float() to convert to float
# print("Type before convertion ", type(name))
# print("Type after convertion ", type(float(name)))
# bytes() to convert to bytes
# print("Type before convertion ", type(name))
# print("Type after convertion ", type(bytes(name, 'utf')))
# # list() to convert to a list object
# my_name = ("Yemi", "Tope", "Sunday")
# print("Type before convertion ", type(my_name))
# print("Type after convertion ", type(list(my_name)))
# set() to convert to a set object
# tuple() to convert to a tuple object
# dict() to convert to a dictionary object
# Example
# value1 = input("enter first number ")
# value2 = input("enter second number ")
# result = int(value1) + int(value2)
# print("the total score is "+ str(result))
# name = "tunde"
# age = "56"
# state = False
# score = 60
# print(float(score))


# Types of Operator
# 1. Arithmetic operator: +, -, /, *, %, //, **
# 2. Assignment operator: =, +=, -=, /=, *=, //=, %=, **=,  etc
# 3. Comparison operator: ==, !=, >, <, <=, >=,
# 4. Logical operator: and, or, not
# 5. Identity operator: is, is not 
# 6. Membership Operators: in, not in 
# 7. Bitwise operator: &, |, ^, ~, <<, >>


# #Arithmetic Operators
# fval = 5 
# sval = 2
# print('for additon '+str(fval + sval))
# print('for subtraction '+str(fval - sval))
# print('for multiplication '+str(fval * sval))
# print('for division '+str(fval / sval))
# print('for modulus '+str(fval % sval))
# print('for exponentiation '+str(fval ** 2))
# print('for floor division '+str(fval // sval))

# #assignment Operators
# fval = 30
# fval +=5           #(fval = fval+5)
# fval -=5
# fval /=5
# fval *=5
# fval %=7
# fval //=7
# fval **=2
# fval >>=5
# fval &=5
# print(fval)
 
 ##########################PERMUTATION CALCULATION###################
# def ref(x):
#     if x ==1:
#         return 1
#     else:
#         return(x * ref(x-1))
# num=int(input("ENTER>> "))
# den=int(input("ENTER>> "))
# okay = ref(num)/ref(num-den)
# print(okay)







# #Comparison Operators
# fval = 10 
# sval = 5
# print(fval == sval)
# print(fval != sval)
# print(fval > sval)
# print(fval < sval)
# print(fval >= sval)
# print(fval <= sval)

# #Logical Operators
# fval = 10 
# sval = 5
# A      B       A and B       A or B       not A

# T      T          T            T           F

# T      F          F            T           F

# F      T          F            T           T

# F      F          F            F           T
# print(fval == sval and fval >= sval)
# print(fval == sval or fval >= sval)
# print(not(fval >= sval))
# print(not(fval >= fval) and ((sval != sval) or (favl > sval)))

# #Identity Operators
# fval = "5" 
# sval = 5
# print(fval is sval)
# print(fval is not sval)

# #Membership Operator
# fval = ["sola", "tunde", "monday", "sunday"]
# comment = "this is a python class for iot and robotics"
# print("monday" in fval)
# print("python" not in comment)

# #Bitwise Operators
# fval = 435645
# sval = 66464
# print(bin(fval))
# print(bin(sval))
# print(bin(fval & sval)) #= 11010010
# print(bin(sval | fval)) # = 11110111
# print(bin(sval ^ fval)) # = 11110111
# print(bin(~ fval)) # = 00001000
# print(bin(sval << 2))
# print(bin(sval >> 2))

# food = input("which food do you have? ")
# if food == "Rice":
#     print("i will buy rice")
# elif food == "Beans":
#   print("i will buy beans")
# elif food == "Yam":
#   print("i will buy yam")
# else:
#   print("i will not buy any food")

# first_number = float(input("Enter your first number>>"))
# operators = input("enter your operator>> ")
# second_number = float(input("Enter your second number>> "))
# if operators == "+":
#     total = first_number + second_number
#     print(total)
# elif operators == "-":
#     total = first_number - second_number
#     print(total)
# elif operators == "*":
#     total = first_number * second_number
#     print(total)
# elif operators == "/":
#     total = first_number / second_number
#     print(total)
# else:
#     print("you enter a wrong operator")


# # Python String Class
name = 'sunday'   #== ['s', 'u', 'n', 'd', 'a', 'y']
# print(name)
# print(type(name))
# print(name[2])
# print(name[0:3])
# print(len(name))
# name2 = "shade"
# value ="234567"
# print(value[2])
# print(len(value))
# comment = """  commented that This is a python class. it was started 
#           last week and still continue through
#           this week. the number of people in this class is   """

# print(comment)
# print(len(comment))
# print(comment[2])
# print(comment[0:9])
# print(comment[-2])
# print(comment[-30:-5])


# String Methods
# print(comment.startswith("commented"))
# print(comment.endswith("is"))
# print("the length of comment is ", len(comment))

# Strip() function
# print('length before strip is ', len(comment))
# print('length after strip is ', len(comment.strip()))


# val1 = float(input("enter value 1 "))
# val2 = float(input("enter value 2 "))
# print('''
# addition
# subtraction'''
# )
# oper = input('enter operation ')
# if oper.strip() == 'addition':
#   print(val1 + val2)
# elif oper.strip() == 'subtraction':
#   print(val1 - val2)
# else:
#   print('invalid selection')
# print(len(value))
# print(len(value.strip()))

# Lower() function
# name = 'SUNDAY'
# print(name.lower())
# value = "method"
# user = input("please enter method to continue ")
# if value == user.lower():
#   print(user)
# else: print("invalid input")

# Upper() function
# value = "METHOD"
# # print(value.upper())
# user = input("please enter method to continue ")
# if value == user.upper():
#   print(user)
# else: print("invalid input")

# # Replace() function
# comment = """  commented that This is a python class. it was started 
#           last week and still continue through
#           this week. the number of people in this class is   """
# newval = comment.replace("commented", "started")
# print(newval)

# Split() function
# print(comment.split())
# print(comment.split('.'))
# print(comment.split('this'))

# Join() function
# word_split = comment.split()
# print(word_split)
# print(" ".join(word_split))
# value = ["rice", "beans", "yam", "banana"]
# print(" ".join(value))

# # Capitalize() function
# comment = """commented that This is a python class. it was started 
#           last week and still continue through
#           this week. the number of people in this class is  """
# print(name.capitalize())
# print(comment.capitalize())
# print(comment.title())
# paul="i am coming\nopal"
# print(paul)
# Center() function
# print(comment.center(10))   

# Count() function
# print(comment.count("week"))

# Encode() function
# print(comment.encode())

# In Operator
# val = "week" in comment
# print(val)
# val = "weak" not in comment
# print(val)

# Concatination
# name = "paul"
# num = 6



# comment = f"""{name} commented that This is a python class. it was started 
#           last week and still continue through
#           this week. the number of people in this class is {num}"""
# print( comment)
# print(comment.format(name, num))
# print(comment)


# # Escape character
# print('she\'s is the owner paul says and i qoute\" GOD IS GOOD \"')
# print('she is the\b owner')
# print('she is the\t owner')

# Array:
#     list
#     tuple
#     set
#     dictionary

# List: is a collection which is ordered and changeable.
#  A list is created with a square bracket [] or list() constructor.
# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
# my_list3 = [1, 45, 54, 23, 67, 78, 46]

# print(my_list2)
# print(my_list[3])
# for name in my_list:
#   print(name)
# my_list[1] = "solar"
# print(my_list)
# print(my_list2[1:4])
# print(my_list2[-3])
# print(my_list2[-4:-1])
# print(len(my_list))
# print(type(my_list2))
# if "energy" in my_list:
#   print("present")
# else:
#   print("not available")
# my_list.append("tunde")
# print(my_list)
# my_list.insert(1, "tunde")
# print(my_list)
# my_list.extend(my_list2)
# print(my_list)
# for name in my_list2:
#   my_list.append(name)
# print(my_list)
# my_list.remove("energy")
# print(my_list)
# my_list2.pop(3)
# print(my_list2)
# my_list2.pop()
# print(my_list2)
# my_list2.clear()
# print(my_list2)
# del my_list2
# print(my_list2)
# my_list3.sort()
# print(my_list3)
# my_list3.sort(reverse=True)
# print(my_list3)
# my_list.sort(reverse=True, key=str.lower)
# print(my_list)
# my_list2.reverse()
# print(my_list2)
# name = my_list2.copy()
# print(name)
# name = list(my_list2)
# print(name)
# name = my_list + my_list2
# print(name)
# print(my_list.count("energy"))
# print(max(my_list3))
# print(min(my_list3))
# print(my_list.index("magnet"))
# my_list4 = [my_list, my_list2,my_list, ['Favour', 34],my_list2, 'Tunde', False]
# print(my_list4)
# [['Shade', 'energy', 'magnet', 'Charse', 'energy'], [12, 14, 'Sunday', 'Charse', True, False, 5.08], ['Favour', 34], 'Tunde', False]
# print(my_list4[2][1:3])

nt = 0
score = 0
question = ["Where is the capital of Nigeria", "Number of states in Nigeria", "Number of LGAs in Nigeria",
            "Who is INEC chairman", "How many political parties participated in 2019 presidential election"]
option = [
           "(a) Lagos \n (b) Kano \n (c) Abuja",
           "(a) 37 \n (b) 36 \n (c) 44",
           "(a) 768 \n (b) 774 \n (c) 780",
           "(a) Prof. Mamhood Yakubu \n (b) Prof. Mohamed Yakub \n (c) Muhamad Yakubu",
           "(a) 18 \n (b) 77 \n (c) 73"
        ]
answer = ["c", "b", "b", "a", "c"]
for que in question:
  print(que)
  print(option[nt])
  ans = input("Your answer > ")
  if ans == answer[nt]:
      score += 5
      print("you are correct")    
  else:
      print("you are wrong")
  nt +=1
print("you total score is ", score)

# Tuple: A tuple is a collection that is ordered but not changeable. A tuple is created using
#  braces i.e () or tuple()
# name = ("Shade", "energy", "magnet", "Charse", "energy")
# name2 = tuple((12, 14, "Sunday", "Charse", True, False, 5.08))
# print(name2)
# print(name[3])
# print(name[1:4])
# print(name[-3])
# print(name[-3:-1])
# print(len(name))
# food = ('Yam',)
# print(food)
# print(type(name2))
# if 12 in name2:
#   print("is available")
# else:
#   print('not available')
# name[3] = "wine"
# name.add("toy") # tuple has no attribute add error
# name.pop() # tuple has no attribute pop error
# del name
# print(name)

# Unpacking values of a tuple
# item = ("Yam", "Sunday", "Lagos","Yam", "Sunday", "Lagos", 45)
# (food, name, location, age) = item
# print(location)
# (food, *name,age,mymy,our) = item
# print(name)
# (food, *name) = item
# print(name)
# for na in name2:
#   print(na)
# new_name = name + name2
# print(new_name)
# new_name = name * 2
# print(new_name)
# print(name.count("energy"))
# print(name.index("magnet"))

# Set: A set is a collection which is unordered and unindexed. It is written using curly bracket
# i.e {} or set()
# name = {"Shade", "energy", "magnet", "Charse",  "Charse", "energy"}
# name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# print(name)
# print(len(name))

# print(type(name2))
# for top in name2:
#     print(top)
# print("magnet" in name)
# print("magnet" not in name)
# name.add("orange")
# print(name)
# name.update(name2)
# print(name)
# new_name = ["food", "drink", "dress", "wears"]
# name.update(new_name)
# print(name)
# name.update(("mango", "apple", "leave"))
# print(name)
# name.remove("Charse")
# print(name)
# name2.discard("Charse")
# print(name2)
# name.pop()
# print(name)
# name.clear()
# print(name)
# del name
# print(name)
# for x in new_name:
#   print(x)

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9} 
# set2 = {2, 4, 5, 7, 8,12}

# set3 = set1.union(set2)
# print(set3)
# set1.update(set2)
# print(set1)
# intercept = set1.intersection((set2))
# print(intercept)
# intercept = set1.intersection((set2)).intersection(set3)
# print(intercept)
# set1.intersection_update(set2)
# print(set1)
# set3 = set1.symmetric_difference(set2)
# print(set3)
# set1.symmetric_difference_update(set2)
# print(set1)
# set1.difference_update(set2)
# print(set1)
# print(set1.isdisjoint(set2))
# print(set1.issubset(set2))
# print(set1.issuperset(set3))

# Dictionary: Dictionary is a collection which is ordered, changeable but does not allows 
# duplicate and unindexed. Dictionary are used to store data in a key:value pairs.
# It is written using {key:value} or dict(key=value)
# product = {'producer':'Toyota', 'model':'venza 2021', 'engine':'6 engine', 'color':'black', 'gear':6, "ok":True}
# student_record = dict(name="Tony Johnson", level=300, course="mechanical engineering", subjects=10)
# print(student_record)
# print(len(product))
# print(type(product))
# print(product["color"])
# print(product.get("producer"))
# print(product.keys())
# print(product.values())
# product["persenger"] = 10
# print(product)
# print(student_record.items())
# print("model" in product)
# product["color"] = "white"
# print(product)
# product.update({"year":2021, "color":"white"})
# print(product)
# product.pop('color')
# print(product)
# product.popitem()
# print(product)
# del product['model']
# print(product)
# product.clear()
# print(product)
# del product
# print(product)
# print(student_record)
# for lol in student_record:
#   print(lol)
# for x in student_record:
#     print(student_record[x])
# for x in student_record.values():
#       print(x)
# for x in student_record.keys():
#   print(x)
# for x, y in student_record.items():
#   print(x , "=", y)
# new_record = product.copy()
# print(new_record)
# new_record = dict(student_record)
# print(new_record)
# student_details = {
#   "Tony Johnson":{'name':'Tony Johnson', 'level':300, 'location':'Takie', 'dept':'math'},
#   "Micheal Chan":{'name':'Micheal Chan', 'level':200, 'location':'General', 'dept':'computer'},
#   "Timi Joy":{'level':400, 'location':'Apake', 'dept':'english'}
# }
# std1 = {'name':"Tony Johnson", 'level':300, 'location':'Takie', 'dept':'math'}
# std2 = {'name':"Micheal Chan", 'level':200, 'location':'General', 'dept':'computer'}
# student_details2 = {
#   'FIRST_PERSON':std1,
#   'SECOND_PERSON':std2
# }
# print(student_details2['FIRST_PERSON'])
# print(student_details["Tony Johnson"])
# print(student_details["Tony Johnson"]['level'])
# for record in student_details2.values():
#   print(record["level"])
# for record in student_details["Tony Johnson"].values():
#   print(record)

# Example:
# student_record = {}
# for i in range(1,3):
#   print("Enter information for student ", i)
#   name = input("Enter your full name >")
#   level = input("Enter your level>")
#   location = input("Enter your location >")
#   dept = input("Enter your department >")
#   student = {"name":name, "level":level, "location":location, "dept":dept}
#   student_record[name] = student

# print(student_record)


# If Else Statement  

# food = input("Madam, what food is available ")
# if food.lower() == 'rice':
#   print("i will buy rice")
# else:
#   print("i will not buy anything")

# Nested if else
# food = input("Madam, what food is available ")
# if food.lower() == "rice":
#   meat = input('what meat is available ')
#   if meat == 'beef' or meat == 'fish':
#       print('i will buy rice today')
#   else:
#       print("i will not buy")
# else:
#   print("i will not buy anything")

# Using multiple Comparison operators
# food = input("What food is available")
# madam = input("What meat is available")
# madam = ("fish", "egg", "beef")
# meat = "fish"
# if food=="rice" and meat in madam:
#   print("i will buy rice")
# else:
#   print("i will not buy anything")

# food = input("Madam, what food is available ")
# if food.lower().strip() == "rice": 
#   print('i will buy rice today')
# elif food.lower() == 'beans':
#   print('i will buy beans today')
# elif food.lower() == 'yam':
#   print('i will buy yam today')
# else:
#   print("i will not buy anything")

#       other = input('what else do you have ')
#       if other == 'egg':
#           print("i will buy rice")
#       else:
#           print('i will check other vendor')
# 
#   option = input('do you hava plantain ')
#   if option.lower() == 'yes':
#       print('i will buy beans today')
# elif food.lower() == 'yam':
#   option = input("do you hava fried egg? ")
#   if option.lower() == 'yes':
#       print('i will buy yam today')
# else:
#   print('i will not buy any food today')

# Pyhon Loop
# while  loop
# x = 0
# while x <= 10:
#     print("hello")
#     x+=1
#     if x == 5:
#         print("You are welcome ", x)        
#         # continue
#         break
#     else:
#         print("The condition was successful")
#         if x == 5:
#             continue
#             print('you are welcome ' , 20)
# else:
#   print("i am done looping")
# Example
# using while loop 
# def menu():
#   print('''
#           1. Daily plan
#           2. Weekly plan
#           3. Monthly plan
#           4. Two months plan
#           5. Three months plan
#           6. back
#         ''')
# ussd = input("please enter your ussd ")
# while ussd != "*131#":
#   reply = input("invalid input!!! please retry again ")
#   if reply == "*131#":
#       break
# menu()
 
# For Loop 
# num = []
# my_ = ["Shade", "energy", "magnet", "Charse", "energy"]
# for name in my_:
#   print(name)
# for x in range(1, 20):
#   val = input("enter your number or q to quit")
#   if val == 'q':
#       break
#   num.append(val)
# else:
#   print(num)
# print(num)
# for m in my_:
#   if m == "magnet":
#       continue
#   print(m)
# for i in range(1, 13):
#   print (i, "Times")
#   for j in range(1, 5):
#       print(str(i) + " times " + str(j) +" = "+ str(i*j))
    
# customer = []
# all_customer = {}
# i = 1
# while i<=10: 
#   info = ['firstName', 'lastName', 'age', 'phone']
#   print("Enter customer "+ str(i) +" infomation")
#   con = input("press 'enter' to continue or 'end' to quit")
#   if con == 'end':
#           break
#   for fo in info:
#       inf = input(fo+": ")
#       customer.append(inf)
#   all_customer["customer"+str(i)] = customer
#   i +=1
# else:
  # for key, value in all_customer.items():
  #   for val in value:
#   print(all_customer)

# Python Functions
# stages of function:
    # function definition: def functionName():
    # function declaration:     print("this is a function to print something to screen")
    # function invocation: functionName()
# val1 = 50
# val2 = 20
# def addition():
#   """
#   addition function is use to add two values together
#   """
#   result = val1 + val2
#   print("the result of this addition is", result)
# addition()


# # Local and Global variables
# def algebral():
#     global val1
#     val3 = 35 
#     val1 = 25
#     res = val1 + val3 * 5
#     print(res)

# def subraction():
#     val3 = 20
#     result = val1 - val3
#     print(result)

# algebral()
# subraction()

# Paramitized and Unparamitized function
# def addition(val3, val4):
#   result = val3 + val4
#   print(result)

# addition(20, 30)
# def subtract(val3, val4=20):
#   print(val3 - val4)

# subtract(50)

# Return Function

# val1 = 50
# val2 = 20
# def subtract(a, b):
#   return a - b
    
# def addition(val3, val4):
#   res = val3 + val4 + subtract(10, 6)
#   return res
# addition(50,20)

# def myName():
#   return "Yemi"
  
# myName()
# c = 8
# def lol():
#       global c
#       c = c + 2
#       print("inside add(): ", c)
# lol()
# print("in main:", c)

# def algebral():
#   add = addition(5, 10)
#   result = val1 + val2 * add
#   print("welcome "+ myName()+ " your score is "+ str(result))

# algebral()

# function Example
# import sys
# func = ""
# def login():
#     user_name = input("Enter your username >")
#     password = input("Enter your password >")
#     if user_name=="Yemi" and password=="1234":
#         operation()
#     else:
#         login()

# def operation():
#     global func
    # print("""Enter your operation:
    #         1. addition
    #         2. subtraction
    #         3. division
    #         4. quit""")
    # option = input(">>> ")
    # if option=="1":
    #     func = "addition"
    #     addition()
    # elif option=="2":
    #     func = "subtract"
    #     subtract()
    # elif option=="3":
    #     func = "division"
    #     division()
    # elif option=="4":
    #     sys.exit()
    # else:
    #     print("Invalid input")
    #     operation()

# def tryAgain():
#     print("Enter 1. perform operation again, 2. go to menu")
#     user = input(">>>")
#     if user=="1":
#         if func=="addition":
#             addition()
#         elif func=="subtract":
#             subtract()
#         elif func=="division":
#             division()
#     elif user=="2":
#         operation()
#     else:
#         print("Invalid input")
#         tryAgain()

# def subtract():
#     val1 = int(input("Enter value 1 >"))
#     val2 = int(input("Enter value 2 >"))
#     print(val1 - val2)
#     tryAgain()
  
# def addition():
#     val1 = int(input("Enter value 1 >"))
#     val2 = int(input("Enter value 2 >"))
#     print(val1 + val2)
#     tryAgain()

# def division():
#     val1 = int(input("Enter value 1 >"))
#     val2 = int(input("Enter value 2 >"))
#     print(val1 / val2)
#     tryAgain()

# login()

# Python Object Oriented Programming (OOP)
# import time
# class Car: 
#     def __init__(self, owner, location):
#         self.owner = owner
#         self.location = location
#         self.name = "Toyota"
#         self.color = "Brown"
#         self.brand = "2019 model"
#         self.trafficator = "straight"
#         self.tyre  = 4
#         self.stiring = 1
#         self.gear = "0"
#         self.details()

#     def details(self):
#         print("""
#             this function show how to calculate or all the details
#             about the car so i low using function 
#         """)
#         print("This car is owned by "+self.owner+ " and is located in "+self.location)
#         time.sleep(2)
#         self.startEnging()

#     def startEnging(self):
#         print("the enging is started")
#         self.gear = input("Enter gear 1 to take off")
#         if self.gear == "1":
#             self.moveCar()
#         else: 
#             print("that is not the right gear to take off")
#             self.startEnging()

#     def moveCar(self):
#         print(self.name+' is in gear '+self.gear +" and the car is moving "+ self.trafficator)
#         self.driver = input("Press Y to change gear or D to chage direction or P to pack")
#         if self.driver.upper() == "Y":
#             self. changeSpeed()
#         elif self.driver.upper() == "D":
#             self.direction()
#         elif self.driver.upper() == "P":
#             self.park()
#         else:
#             self.moveCar()

#     def changeSpeed(self):   
#         self.gear = input("Enter gear number ")
#         if self.gear == "1":
#            self.moveCar()
#         elif self.gear == "2":
#             self.moveCar()
#         elif self.gear == "3":
#             self.moveCar()
#         elif self.gear == "4":
#             self.moveCar()

#     def direction(self):
#         self.trafficator = input("please enter your direction ")
#         if self.trafficator.lower() == "straight":
#             self.moveCar()
#         elif self.trafficator.lower() == 'left':
#             self.moveCar()
#         elif self.trafficator.lower() == 'right':
#             self.moveCar()
   
#     def park(self):
#         print('the car is parking now ...')
#         time.sleep(2)
#         print("The car has finished parking and appliction exited")

# cr = Car("Smith", "Ogbomoso")

# Python Inheritance 
# class Father:
#   def __init__(self):
#       self.family_name = "Adeowo compound"
#       self.name = "Owolabi"
#       self.skin_color = "dark skin"
#       self.height = "tall"
#       self.language = "Yoruba"

#   def walk(self):
#       print(self.name+ " from "+self.family_name+" is walking")
  
#   def talk(self):
#       print(self.name +' from '+self.family_name+' is talking')
  
#   def sleep(self):
#       print(self.name +' is still sleeping')
    
# class Child(Father):
#     def __init__(self):
#         # Father.__init__(self)
#         super().__init__()
#         self.birth = "2003"
#         self.location = "Ogbomoso"
#         self.name = "Johnson"
    
#     def run(self):
#         print(self.name+ " is running up and down")

# class GrandChild(Child):
#     def __init__(self):
#         # super().__init__()
#         self.name = "Micheal"
#         self.family_name = "oyo"

# ch = Child()
# print(ch.language)
# ch.walk()
# gd = GrandChild()
# gd.run()
# gd.walk()

# Python Module  
# import os
# import sys
# import time
# print(dir(time))
# print(help())

# Python Database (Mysql)
# To download mysql connector user: pip install mysql-connector
# import mysql.connector
# mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='', database='cbtTest_db')

# mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE cbtTest_db")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE customers (ctm_id INT(4), Ful_Name VARCHAR(20), Address VARCHAR(50), Phone VARCHAR(11), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")

# for table in mycursor: 
#     print(table)

# mycursor.execute("ALTER TABLE customers CHANGE ctm_id ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE customers ADD UNIQUE(Phone);")

# myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = ('Timi Adesola', 'Owolake', '07067307758', '12345')
# mycursor.execute(myquery, val)
# mycon.commit()

# fulname = input('enter your name >') 
# address = input('enter your address')
# phone = input('enter your phone number')
# password = input('enter your Password')
# myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = (fulname, address, phone, password)
# mycursor.execute(myquery, val)
# mycursor.executemany((myquery, val),(),())
# mycon.commit()
# print(mycursor.rowcount, "records inserted successfully")

# query = "SELECT * FROM customers"
# mycursor.execute(query)
# output = mycursor.fetchall()
# print(output)
# for inf in output:
#   print(inf)
# query = "SELECT * FROM customers WHERE Phone=%s"
# query = "SELECT * FROM customers WHERE Ful_Name LIKE '%th%'"
# query = "SELECT Ful_Name, Phone FROM customers"
# query = "SELECT * FROM customers ORDER BY ful_Name DESC"
# val = ('09013140700', val)
# phone = input("Enter your phone number ")
# pin = input("Enter your pin ")
# query = "SELECT Phone, Password FROM customers WHERE Phone=%s AND Password=%s"
# val = (phone, pin)
# mycursor.execute(query, val)
# myreg = mycursor.fetchall()
# # myreg = mycursor.fetchone()
# print(myreg)
# for info in myreg:
#     print(info)
# mycon.commit()
# print(mycursor.rowcount, 'selected successfuly')
# mycon.close()

# sql = "UPDATE customers SET  Password='2123' WHERE Phone=%s"
# val =('08056524121',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record updated successfuly')

# sql = "DELETE FROM customers WHERE Phone=%s"
# val =('08056524121',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record deleted successfuly')

# sql = "DROP TABLE customers"
# mycursor.execute(sql)

# PDF Drive

# File Handling
# myFile = open("filename", mode='r', 'a', 'w','x', encoding='t','b')
# 'r' read only and it is the default for open function. Raise error if file does not exist
# 'a' Append new content to an existing file. Create new file with the specified name if file does not exist.
# 'w' Open file for writing. Create new file with the specified name if file does not exist
# 'x' To create new file. Raise error if file already exist

# with open("filename", mode="rt") as myFile:

# myFile = open("C:\\Users\\YEMI\\Documents\\pyhon code.txt", 'rt')
# myFile = open("C:\\Users\\D\\Documents\\DATA SCI_CLASS\\pythonbasicclass\\damilare.html", 'rt')
# print(myFile.read())
# print(myFile.read(20))
# print(myFile.readline())
# print(myFile.readlines())
# for i in range(20):
#     print(myFile.readline())
# for text in myFile:
#     print(text)
# myFile.close()

# myFile = open("C:\\Users\\D\\Documents\\DATA SCI_CLASS\\pythonbasicclass\\damilare.html", 'rt')
# print(myFile)
# myFile.write("\n this is a new content to append to the old file")

# myFile = open("infile2.txt", 'rt')
# print(myFile.read())
# myFile.close()

# myFile = open("infile.txt", 'w')
# myFile.write("\n this is a new content to append to the old file")

# myFile = open("infile.txt", 'rt')
# print(myFile.read())
# myFile.close()

# using with open function
# with open("C:\\Users\\D\\Documents\\DATA SCI_CLASS\\pythonbasicclass\\damilare.html", mode="rt") as myFile:
#     print(myFile.read())

# import os
# if os.path.exists("C:\\Users\\D\\Documents\\DATA SCI_CLASS\\pythonbasicclass\\damilare.html"):
# 	with open("C:\\Users\\D\\Documents\\DATA SCI_CLASS\\pythonbasicclass\\damilare.html", mode="rt") as myFile:
# 		print(myFile.read())
# else:
# 	print("file does not exits")

# if os.path.exists("C:\\Users\\D\\Documents\\DATA SCI_CLASS\\pythonbasicclass\\damilare.html"):
#     os.remove("C:\\Users\\D\\Documents\\DATA SCI_CLASS\\pythonbasicclass\\damilare.html")
#     print("file deleted successfully")
# else:
#     print("file not available.")
# os.mkdir("new folder")
# os.rmdir("Documents")

# code to remove folder containing contents in it
# for root, dirs, files in os.walk("Documents"):
#     for file in files:
#     	os.remove("Documents\\"+file)
# os.rmdir("Documents")

# code to get username of any system(pc)
# import os.path
# homedir = os.path.expanduser("~")
# print(homedir)
# code to get system environment
# import os
# homedir = os.environ["PATH"]
# print(homedir)

# code to get the path of a file on your device
# print(os.path.dirname(os.path.abspath("damilare.py")))


# Python Error Handling
# Two types of error in programming:
# compile time error and run time error
# try and except, finally 

# def simpleCal():
# 	for i in range(5):
# 		a = int(input("enter quotient value"))
# 		b = int(input("enter divisor value"))
# 		print(a/b)
# simpleCal()

# def cal(): 
#     for i in range(5):
#         a = int(input("enter quotient value"))
#         b = int(input("enter divisor value"))
#         try:
#             print(a/b)
#         except:
#             print("divisor can not be zero")
# cal()

# def cal(): 
#     for i in range(5):
#         a = int(input("enter quotient value"))
#         b = int(input("enter divisor value"))
#         try:
#             print(a/b)
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except TypeError:
#             pass
#         except:
#             pass
#         else: # execute if no error was raised
#             print("no error was raised")
#         finally: # execute either there is error or not
#             print("the execution was successful")
# cal()

# a = int(input("enter quotient value"))
# b = input("enter divisor value")
# if type(b) is not int:
#     raise TypeError("divisor must be an integer type")
# else:
#     print(a/b)


# Python Regular Expression
# import re
# text = """the value of a thing will determing the capacity you put to it. the value of 2019 is what you get in 2020
#         and now you get the value of 2020 in 2021"""
# mm ="""the  get"""
# val = re.search("^the.*get$", mm)
# if val:
#     print("We have a match")
# else:
#     print("No match detected")
 
# re function
# findall() : returns list containing all matches
# search() : returns object of a match if there is a match anywhere in the string
# split() : returns a list where the string has been split at each match
# sub() : replace one or many matches  with a string

# re matacharacters
# [] : refers to set of characters to match eg "[a-m]"
# \ : can be use to escape special charactter eg "\d"
# . : any character except newline character eg 'he.o'
# ^ : starts with eg "^the"
# $ : ends with eg "world$"
# * : zero or more occurrences eg "aix*"
# + : one or more occurrences eg "aix+"
# {} : exactly specified number of occurrence eg "al{2}"
# | : either or eg "this|that"
# () : capture and group 

# re special Sequences
# \A : returns a match if the specified characters are at the begining of the string eg "\AThe"
# \b : returns a match if the specified characters are at the begining or at the end of the string eg r"\bthe" or r"the\b"
# \B : returns a match if the specified characters are present but not at the begining or at the end of the string eg r"\Bthe" or r"the\B"
# \d : returns a match where the string contains digits (number from 0-9) eg "\d"
# \D : returns a match where the string does not contains digits eg "\D"
# \s : returns a match where the string contains a white space character eg "\s"
# \S : returns a match where the string does not contains a white space character eg "\S"
# \w : returns a match where the string contains characters from letter A-Z and digits from 0-9 and underscore eg "\w"
# \W : returns a match where the string does not contains any word characters 
# \Z : returns a match if the specified characters are at the end of the string

# re sets
# [arn] : returns a match where one of the specified characters (a or r or n ) are present
# [a-n] : returns a match for any lower case character alphabetically between a and n
# [^arn] : returns a match for any character except a, r and n
# [0123] : returns a match where any of the specified digits (0, 1, 2, 3) are present
# [0-9] : returns a match for any digits between 0 and 9
# [0-5][0-9] : returns a match for any two digits between 00 and 59
# [a-zA-Z] : returns a match for any character alphabetically between a and z lower case or upper case
# [+] : returns a match for any character in the string

# x = re.findall(r'the', text)
# print(x)
# x = re.search(r'you', text)
# print(x)
# print(x.span())
# print(x.group())
# print(x.string)
# z = re.split(r'\s', text)
# print(z)
# z = re.split(r'\s', text, 5)
# print(z)
# tx = re.sub(r'\d', '[]', text)
# print(tx)
# tx = re.sub(r'capacity', 'ability', text)
# print(tx)
# tx = re.sub(r'\d', '[]', text, 4)
# print(tx)

# Python DataTime
# import datetime
# tim = datetime.datetime.now()
# print(tim)
# print(tim.year)
# print(tim.strftime("%A"))
# tm = datetime.datetime(2021, 4, 10)
# print(tm)
# print(tm.month)
# tm = datetime.datetime(2021, 4, 10, 12, 30, 20,8)
# print(tm)
# strftime() method - use to format datetime object into readable string
# print(tm.strftime("%Z"))
# # strftime format codes
# %a : returns weekday in short version eg wed
# %A : returns weekday in full version eg wednesday
# %w : returns weekday in number version from 0-6 where 0 means sunday eg web is 3 
# %d : returns day of the month in number version from 01-31
# %b : returns month name in short version eg Dec
# %B : returns month name in full version eg December
# %m : returns month in number formart from 01-12 
# %y : returns year in short version eg 2021 is 21
# %Y : returns year in full version eg 2021
# %H : returns hour in 24hrs format from 00-23
# %I : returns hour in 12hrs format from 00-12
# %p : returns AM or PM of time
# %M : returns minute of time from 00-59
# %S : returns seconds of time from 00-59
# %f : returns microseconds of time form 000000-999999
# %Z : for timezone
# %j : days number of the year from 001-366
# %U : return week number of the year from 00-54 
# import vlc
# import time
# # print(help(vlc.AudioSetVolumeCb))
# # print(help(vlc.MediaPlayer))

# while True:
#     time.sleep(5)
#     tm = datetime.datetime.now()
#     if tm.strftime("%I") == "9" or tm.strftime("%M") == "56" or tm.strftime("%S") == "04" and tm.strftime("%p") == "AM":
#         # if tm.strftime("%M") == "51":  
#         print("it's time for break")
#         break
#         #/'' p = vlc.MediaPlayer("01 Merciful God.mp3")
#         # p.play()
#         # time.sleep(170)
#         # p.stop()
#         # break
#     else:
#         print("lecture continues") 
        # p = vlc.MediaPlayer("01 Merciful God.mp3")
        # p.play()
        # time.sleep(170)
        # p.stop()
        # break      
        
        

# import datetime
# check = int(datetime.datetime.now().strftime("%M")) 
# # print(check)
# rang =[]
# [rang.append(rn) for rn in range(0,60)]
# while True:
#     time =datetime.datetime.now() 
#     nexttime = time.strftime('%M')
#     # print(nexttime)
#     if int(nexttime) in rang and check == int(nexttime):   
#         for i in range(1):
#             print("i am going for class today")
#     check = int(nexttime )+ 1

# hour = hour[0]+str(int(hour[1]) + 2)
# print(hour)

# Python Math class
# import math
# print(help(math.ceil))
# l = [2, 4, 5, 7, 3]
# print(min(l))
# print(max(l))
# print(abs(-5.34))
# print(pow(3, 3))
# print(math.sqrt(9))
# print(math.ceil(8.3492))
# print(math.floor(5.6732))
# print(math.pi)
# print(math.pi * 1000 + 25)


# import vlc
# import time

# p = vlc.MediaPlayer("01 Merciful God.mp3")
# p.play()

# time.sleep(123)
# p.stop()



# import re
# regex ="^[a-z0-9]+[@]\w+[.]\w{3,3}$"
# email = input("Enter your Email>>")
# verify = re.findall(regex, email)
# if verify:
#   print(email)
# else:
#   print("noting")



# working with openCV
# installing using Anaconda 
# conda install -c conda-forge opencv

# install on windows
# pip install opencv-python


# cv2.imread(path, flag)

# import cv2
# img =cv2.imread("name.jpg"or"name.png",1)
# to display the image
# cv2.imshow('imagename', img)
# cv2.waitkey()
# cv2.destroyAllWindows()



# inwrite function in openCV
# cv2.inwrite(filename, image)
# img=cv2.imread(r'C:Users\p\nammn.jpeg', img )
# print("image writeen sucess?: ", status)


# ACCESS PIXEL VALUES AND MODIFY THEM
# import numpy as np
# import cv2 as cv
# img = cv.imread(r 'C\Users\....\dog.jpeg' )
# px = img[100,100]
# print(px)
# acess color of the pixel
# blue =img[100,100,0]
# print(blue)

# img[100,100] =[255,255,255]
# print(img[100,100])

# img.item(10,10,2)
# Modify the red value
# img.itemset((10,10,2),100)
# img.item(10,10,2)

# Access the image properties
# print(img.shape)
# print(img.size)

# to check the dtype of the img
# print(img.dtype)























