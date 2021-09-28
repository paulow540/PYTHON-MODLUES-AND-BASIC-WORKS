# import re

# m = re.match('foo', 'seafood')     # no match >>> 
# if m is not None:
#     m.group() 
#     print(m)

# m=re.match('foo', 'on food the table').group()
# print(m)

# m = re.search('foo', 'seafood').group()   # use search() instead >>> 
# print(m)

# Matching More than One String (|)
# bt = 'bat|bet|bit'             # regex pattern: bat, bet, bit >>>
# m = re.match(bt, 'bat').group()       # 'bat' is a match >>> 
# print(m)

# m = re.match(bt, 'blt')        # no match for 'blt' >>> 
# if m is not None: m.group() 
# m = re.match(bt, 'He bit me!') # does not match string >>> 
# if m is not None: m.group() 
# m = re.search(bt, 'He bet me!') # found 'bit' via search >>> 
# if m is not None: m.group()
# print(m)

# email = input("Enter Email>")
# patt = '\w+@(\w+\.)?\w+\.com' 
# conemail = re.match(patt, email).group() 
# if conemail is not None:
#     print("valid")
# else:
#     print("invalid")


# m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
# m.group()                       # entire match 'abc-123' >>> 
# m.group(1)                      # subgroup 1 'abc' >>> 
# m.group(2)                     # subgroup 2 '123' >>> 
# # m.groups()                      # 


# DATA = (    
#     'Mountain View, CA 94040',      
#     'Sunnyvale, CA', 
#     'Los Altos, 94023', 
#     'Cupertino 95014', 
#     'Palo Alto CA',  ) 
# for datum in DATA:     
#     print (re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))


#!/usr/bin/env python 
# import os 
# from distutils.log import warn as printf

# with os.popen('who', 'r') as f:
#     for eachLine in f: 
#         printf(re.split(r'\s\s+|\t', eachLine.rstrip()))
# f.close()







# from socket import *  
# from time import ctime  
# HOST = '' 
# PORT = 21567  
# BUFSIZ = 1024  
# ADDR = (HOST, PORT) 
# tcpSerSock = socket(AF_INET, SOCK_STREAM) 
# tcpSerSock.bind(ADDR)  
# tcpSerSock.listen(5)  
# while True:
#     print ('waiting for connection...' ) 
#     tcpCliSock, addr = tcpSerSock.accept()  
#     print ('...connected from:', addr) 
#     while True:
#         data = tcpCliSock.recv(BUFSIZ) 
#         if not data:
#             break 
#         tcpCliSock.send('[%s] %s' % (   
#         ctime(), data)) 
#     tcpCliSock.close()  
# tcpSerSock.close()



# from __future__ import print_function
# print(help(print_function))

# import turtle
# ninja = turtle.Turtle()
# ninja.speed(3)
# for i in range(180):    
#     ninja.forward(100)    
#     ninja.right(30)    
#     ninja.forward(20)    
#     ninja.left(60)    
#     ninja.forward(50)    
#     ninja.right(30)       
#     ninja.penup()    
#     ninja.setposition(0, 0)    
#     ninja.pendown()       
#     ninja.right(2)   
# turtle.done()

# import os
# print(help(os.path))
# p = os.path.join(os.getcwd(), 'oloniaye.py')
# print(p)

# first = input("ENTER YOUR NAME>>")
# second =first.lower()
# print(second)
# print(second[0:2])

import re
email = input("Enter your email")
regex ="^[a-z0-9]+[@]\w+[a-z]\w+[.]\w{3,3}$"
varify = re.findall(regex,email)
if varify:
    print(email)
else:
    print("non")









