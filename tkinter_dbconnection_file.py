from logging import exception
#from sqlite3 import Cursor
from mysql.connector.cursor import MySQLCursor


class mysqlCon:
    conn = ""

    def __init__(self):  # self represents the instance of the class. Usage of "self" in class to access the methods and attributes

        print("This is as an initializer method of class mysqlCon ...")

    def fndbconn(self):
        global conn

        # Importing the connector class from MySql.
        import mysql.connector as mysqlConnector

        conn = mysqlConnector.connect(
            host='localhost', user='root', password='rootroot1234', database='PythonWordle')  # We access the connect method through the connector class, which we already import into our program. Now, we are passing our connection parameters to the connect method. The user name and password will be different according to your installation process.
        if conn:
            return 1
        else:
            return 0

    def fnLogin(self, tmpuser, tmppass):
        global conn
        # Importing cursor method from the established connection (conn) object and createing the cursor object mycursor to use in code.
        mycursor = conn.cursor()

        print(f"Entered Username = {tmpuser}")
        print(f"Entered Password = {tmppass}")

        tuple1 = (tmpuser, tmppass)

        query = """select * from users where username=%s and password=%s"""
        # The execute () method helps us to execute the query and return records according to the query.
        result = mycursor.execute(query, tuple1)
        # Returns the all or remaining rows from the result set.
        result = mycursor.fetchone()
        print(f"Result = {result}")

        return result

    def fnRegister(username, password, tmpemailid):
        mycursor = conn.cursor()
        print(username, password, tmpemailid)
        mycursor.execute(
            f"insert into users(username,password,email_id) values('{username}','{password}','{tmpemailid}')")
        conn.commit()
        conn.close()
