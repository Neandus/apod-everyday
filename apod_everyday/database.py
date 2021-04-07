"""
There are at least 3 ideas how to tackle problem of wrapping database.
1. Use __init__ and __del__ methods responsible for open and close connection,
keeping it open until object gets deleted or goes out of scope.
2. Use __enter__ and __exit__ methods along with 'with' keyword to open and close
connection just in place (with statement).
3. The most thoughtful way I found is to use class object for connection (singleton),
set the object on first instance of the class and delete only on exit.
Then each class instance uses the connection as their own.

Solution copied from:
https://softwareengineering.stackexchange.com/questions/200522/how-to-deal-with-database-connections-in-a-python-library-module/358061
"""

import psycopg2
import os

class Postgres(object):
    """docstring for Postgres"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            db_config = config()
            try:
                print('connecting to PostgreSQL database...')
                connection = Postgres._instance.connection = psycopg2.connect(**db_config)
                cursor = Postgres._instance.cursor = connection.cursor()
                cursor.execute('SELECT VERSION()')
                db_version = cursor.fetchone()

            except Exception as error:
                print(f'Error: connection not established {error}')
                Postgres._instance = None

            else:
                print(f'connection established\n{db_version[0]}')

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def query(self, query):
        try:
            result = self.cursor.execute(query)
        except Exception as error:
            print(f'error execting query "{query}", error: {error}')
            return None
        else:
            return result

    def __del__(self):
        self.connection.close()
        self.cursor.close()

if __name__ == "__main__":
    pass