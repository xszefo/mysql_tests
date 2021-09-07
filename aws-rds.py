#!/usr/bin/env python

import mysql.connector
from settings import user,password

def main():
    host = 'database-1.civ0gy3qgtaf.eu-central-1.rds.amazonaws.com'
    db = 'myDB'

    print(f'Connecting: {host} to database {db}')
    cnx = mysql.connector.connect(user=user, 
                                  password=password,
                                  host=host,
                                  database=db)
    cursor = cnx.cursor()

    table = 'currencies'
    try:
        commands = [f'DESCRIBE {table};',f'SELECT * FROM {table};']

        for cmd in commands:
            cursor.execute(cmd)
            print(cmd)
            for i in cursor:
                print(i)

    finally:
        print(f'Disconnecting: {host}')
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    main()
