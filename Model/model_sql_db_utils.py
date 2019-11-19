###########################################################################
#
#   model_sql_db_utils.py
#   sqlite3 implementation framework by "Adam McQuistan" (https://stackabuse.com/a-sqlite-tutorial-with-python/)
#
#   Edited by: David K. Hwang
#
#
############################################################################

import os
from pysqlcipher3 import dbapi2 as sqlcipher
from datetime import datetime


## 7 lines below this comment are from "Adam McQuistan" (link at page header)
# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'InvApp.database_encrypt')


# function to return whether the database file for application use has been created or not
def db_isPresent(db_path=DEFAULT_PATH):
    return os.path.exists(db_path)


# creates the db connection and returns the connection and cursor
def db_create_connection(db_pass, db_path=DEFAULT_PATH):
    db_conn = sqlcipher.connect(db_path)
    db_cur = db_conn.cursor()
    db_cur.execute("PRAGMA key='" + db_pass + "'")
    return db_conn, db_cur


# creates the database file and initializes it with the default table parameters
def db_firstTimeCreate(db_pass, db_path=DEFAULT_PATH):
    db_conn = sqlcipher.connect(db_path)   # connect to db @ db_path location
    db_cur = db_conn.cursor()            # init cursor object to execute SQL statements

    # create strings to define tables
    sql_createTable_Clients = """CREATE TABLE IF NOT EXISTS Clients (
                                    Id integer PRIMARY KEY,
                                    Name nvarchar(128) NOT NULL,
                                    Address nvarchar(256) NOT NULL,
                                    Phone nvarchar(24),
                                    Email nvarchar(128),
                                    DateAdded timestamp);"""

    # execute the creation of a table
    db_cur.execute("PRAGMA key='" + db_pass + "'")
    db_cur.execute(sql_createTable_Clients)
    db_conn.commit()
    return db_conn, db_cur


def db_newClient_test(db_conn):
    db_cur = db_conn.cursor()    # create cursor object from db connection

    # execute insert into newly created table

    sql_tableInsert_Clients = "INSERT INTO Clients(Id, Name, Address, Phone, Email, DateAdded) values (?,?,?,?,?,?)"
    db_cur.execute("PRAGMA key='password'")
    db_cur.execute(sql_tableInsert_Clients, (1, "Name1", "Address1", "7183497234", "email1", datetime.now()))
    db_conn.commit()
    db_cur.close()


def db_printAllClients(db_conn):
    db_cur = db_conn.cursor()
    db_cur.execute("SELECT * FROM Clients")
    #print(db_cur.fetchone())


def db_connectionCheck(db_conn):
    connected = False
    try:
        db_printAllClients(db_conn)
        connected = True
        return connected
    except:
        return connected
