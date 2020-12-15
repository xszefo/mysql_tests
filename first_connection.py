#!/usr/bin/env python

from settings import user,password
import mysql.connector


cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='test1')
cursor = cnx.cursor()

table = 'currencies'

#command = 'CREATE TABLE currencies (name VARCHAR(10), code VARCHAR(3));'
describe = f'DESCRIBE {table}'
select = f'SELECT * FROM {table};'

#cursor.execute(command)
#cursor.execute(describe)
#for row in cursor:
#	print(row)
cursor.execute(select)
for i in cursor:
	print(i)

insert = f"INSERT INTO {table} VALUES ('dollar', 'USD');"
cursor.execute(insert)

insert = f"INSERT INTO {table} VALUES ('euro', 'EUR');"
cursor.execute(insert)

cursor.execute(select)
for i in cursor:
	print(i)

cnx.commit()

cursor.close()
cnx.close()

