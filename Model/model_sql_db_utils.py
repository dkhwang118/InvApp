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
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'InvApp.database')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlcipher.connect(db_path)
    return con


# creates the database file and initializes it with the default table parameters
def db_create(db_path=DEFAULT_PATH):
    db_con = sqlcipher.connect(db_path)   # connect to db @ db_path location
    db_cur = db_con.cursor()            # init cursor object to execute SQL statements

    # create strings to define tables
    sql_createTable_Clients = """CREATE TABLE IF NOT EXISTS Clients (
                                    Id integer PRIMARY KEY,
                                    Name nvarchar(128) NOT NULL,
                                    Address nvarchar(256) NOT NULL,
                                    Phone nvarchar(24),
                                    Email nvarchar(128),
                                    DateAdded timestamp);"""

    # execute the creation of a table
    db_cur.execute(sql_createTable_Clients)

    return db_cur


def db_newClient_test(db_cur):
    #db_cur = db_con.cursor()    # create cursor object from db connection

    # execute insert into newly created table
    sql_tableInsert_Clients = "INSERT INTO Clients(Id, Name, Address, Phone, Email, DateAdded) values (?,?,?,?,?,?)"
    db_cur.execute(sql_tableInsert_Clients, (1, "Name1", "Address1", "7183497234", "email1", datetime.now()))


def db_printAllClients(db_cur):
    #db_cur = db_con.cursor()
    print(db_cur.fetchone())

