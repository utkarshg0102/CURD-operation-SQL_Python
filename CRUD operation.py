#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Connection to a SQL"""

import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user= 'root', passwd = 'password@01')

print(mydb)

if mydb:
    print("Connection established")
else:
    print("Connection is not established")


# In[ ]:


"""Create Database""" 

mycursor = mydb.cursor()
mycursor.execute("create database SQL_Python")

print("Data base created succesfuly")


# In[ ]:


""" To see all databases available in SQL"""

mycursor = mydb.cursor() 
mycursor.execute("Show databases")

for db in mycursor1():
    print(db)


# In[ ]:


"""Create Table in the created database"""

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "password@01", database = "sql_python")

mycursor = mydb.cursor() 
mycursor.execute("create table CRUD_Operation(name varchar(200), salary int(20))")


# In[ ]:


"""Insert values in to the database"""

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "password@01", database = "sql_python")

mycursor = mydb.cursor()
sqlform = "Insert into CRUD_Operation(name,salary) values(%s,%s)"
CRUD_Operation = [("Harshit", 20000),("amit", 30000),("ankita",40000),]
mycursor.executemany(sqlform,CRUD_Operation)
mydb.commit()


# In[ ]:


"""Read Operation -> fetchall"""

mycursor = mydb.cursor()
mycursor.execute("select * from CRUD_Operation")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)


# In[ ]:


"""Read Operation -> fetchone"""

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "password@01", database = "sql_python")

mycursor = mydb.cursor()
mycursor.execute("select name from CRUD_Operation")
myresult = mycursor.fetchone()

for row in myresult:
    print(row)


# In[ ]:


"""Read Operation -> fetchone"""

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "password@01", database = "sql_python")

mycursor = mydb.cursor()
mycursor.execute("select name from CRUD_Operation")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)


# In[ ]:


"""Update operation"""

mycursor = mydb.cursor()
sql = "UPDATE CRUD_Operation set salary = 50000 where name = 'ankita'"
mycursor.execute(sql)
mydb.commit()

# Now to check if the update operation has worked or not do read operation here...

mycursor.execute("select * from CRUD_Operation")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)


# In[ ]:


"""Delete operation"""

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "password@01", database = "sql_python")

mycursor = mydb.cursor()
sql = "DELETE from CRUD_Operation where name = 'amit'"
mycursor.execute(sql)
mydb.commit()

# To check it follow read operation:

mycursor = mydb.cursor()
sql = "select * from CRUD_Operation"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for row in myresult:
    print(row)


# In[ ]:




