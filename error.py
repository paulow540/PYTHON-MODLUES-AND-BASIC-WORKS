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
# val = re.search("^the.*get$", text)
# if val:
#     print("We have a match")
# else:
#     print("No match detected")
 

import re
class Questions:
    def __init__(self):
         self.menu()

    
    def admin(self):
        seldadmin_name ="opakunbi paul"

    def student(self):
        self.studentName= input("Enter ypur name>>")
        self.studentEmail =input("Enter ypur Email>>")
        self.approveemail =re.macth([A-Za-z0-9])
        # query ="InSERT INTO studen_info (name,email) values= %s,%s"
        # vaqlue =(self.studentName,self.approveEmail)


    def menu(self):
        print("""1. Student for the exam\n2. Admin""")
        self.choose =input("Enter to choose>>")
        if self.choose == "1":
            self.student()


reg = Questions()
