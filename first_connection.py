#!/usr/bin/env python

from settings import user,password
import mysql.connector


cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database='employees')
cnx.close()

