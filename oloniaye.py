import mysql.connector
mycon =mysql.connector.connect(host="127.0.0.1", user="root",passwd="",database="myicon_db")

mycursor=mycon.cursor()

# mycursor.execute("CREATE DATABASE mmmmkkkkk")
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

# mycursor.execute("CREATE TABLE mytable (cts_id INT(4), First_name VARCHAR(20), Seond_name VARCHAR(20), Password VARCHAR(10))")
# mycursor.execute("SHOW TABLES")
# for i in mycursor:
#     for x in i:
#         print(x)
# mycursor.execute("ALTER TABLE mytable CHANGE cts_id cts_id INT(4) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE mytable ADD UNIQUE(Password)")

# query =("INSERT INTO mytable (First_name,Seond_name,Password) VALUES(%s,%s,%s)")
# val = ("opakunbi","paul","1234")
# mycursor.execute(query,val)
# mycon.commit()

# fulname = input('enter your name >') 
# second = input('enter your address')
# phone = input('enter your phone number')
# password = input('enter your Password')
# myquery = "INSERT INTO mytable (First_name,Seond_name,Password) VALUES(%s, %s, %s)"
# val = (fulname,  second, password)
# mycursor.execute(myquery, val)
# # mycursor.executemany((myquery, val),())
# mycon.commit()
# print(mycursor.rowcount, "records inserted successfully")

# query = "SELECT * FROM mytable"
# mycursor.execute(query)
# output = mycursor.fetchall()
# print(output)

# sql = "DELETE FROM mytable WHERE Password=%s"
# val =('08056524121',)
# mycursor.execute(sql, val)
# mycon.commit()

sql = "DROP DATABASE myicon_db"
mycursor.execute(sql)