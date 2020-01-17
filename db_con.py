# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:58:12 2020

@author: ritu raj
"""
import mysql.connector as ms1
ms2=ms1.connect(host='localhost',user='ritu raj',passwd='123qwe,./',database='py_tes')
ms=ms2.cursor()
#def check_id(name):
   # ms.execute('select id from employee where name="%s"'%name)
   # id1=ms.fetchall()
   # return id1[0][0]
#ms.execute('show databases')
#for i in ms:
#    print(i)
#cursor= ms2.cursor()

#result = cursor.fetchall()

#for i in range(len(result)):
#	print(result[i])
ms.execute('SHOW TABLES')
for i in ms:
    print(i)
#mySql_insert_query = """INSERT INTO employee (Id, Name, age, salary) 
                         #  VALUES 
                          # (3, 'mayank', 24, '500') """

   # ms = ms2.cursor()
#ms.execute(mySql_insert_query)
#ms.commit()
#print(ms.rowcount, "Record inserted successfully into employee table")
   # cursor.close()
   
#cursor = conn.cursor()
count=0
ms.execute('SELECT * FROM employee')
for i in ms:
    count+=1

    print(i)
print(count)
    

   