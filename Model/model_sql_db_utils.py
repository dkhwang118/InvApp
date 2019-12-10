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
import sys
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
def create_connection(db_pass, db_path=DEFAULT_PATH):
    db_conn = sqlcipher.connect(db_path)
    db_cur = db_conn.cursor()
    db_cur.execute("PRAGMA key='" + db_pass + "'")
    return db_conn, db_cur


# creates the database file and initializes it with the default table parameters
def firstTimeCreate(db_pass, db_path=DEFAULT_PATH):
    db_conn = sqlcipher.connect(db_path)   # connect to db @ db_path location
    db_cur = db_conn.cursor()            # init cursor object to execute SQL statements

    # create strings to define tables
    sql_createTable_Clients = """CREATE TABLE IF NOT EXISTS Clients (
                                    Id integer PRIMARY KEY,
                                    Name TEXT UNIQUE NOT NULL,
                                    Address_line1 nvarchar(128) NOT NULL,
                                    Address_line2 nvarchar(128) NOT NULL,
                                    Phone nvarchar(24),
                                    Email nvarchar(128),
                                    DateAdded timestamp);"""

    sql_createTable_Products = """CREATE TABLE IF NOT EXISTS Products (
                                    Id integer PRIMARY KEY,
                                    Name TEXT UNIQUE NOT NULL,
                                    Description TEXT,
                                    PriceInCents INT NOT NULL,
                                    DateAdded timestamp);"""

    sql_createTable_Orders = """CREATE TABLE IF NOT EXISTS Orders (
                                    Id INTEGER PRIMARY KEY,
                                    ClientId INTEGER NOT NULL,
                                    FullOrderNumber TEXT UNIQUE NOT NULL,        
                                    OrderYear INTEGER NOT NULL,
                                    OrderMonth INTEGER NOT NULL,
                                    OrderNumber INTEGER NOT NULL,
                                    DeliveryDate TEXT,
                                    SubTotal INTEGER NOT NULL,
                                    OrderPaid INTEGER NOT NULL,
                                    OrderPaidDate TEXT,
                                    CreatedDate timestamp,
                                    FOREIGN KEY (ClientId) REFERENCES Clients (Id));"""

    sql_createTable_OrderItems = """CREATE TABLE IF NOT EXISTS OrderItems (
                                    ProductId INTEGER NOT NULL,
                                    OrderId INTEGER NOT NULL,
                                    NumInOrder INTEGER NOT NULL,
                                    PRIMARY KEY (ProductID, OrderId),
                                    FOREIGN KEY (ProductId) REFERENCES Products (Id),
                                    FOREIGN KEY (OrderId) REFERENCES Orders (Id));"""

    # execute the creation of a table
    db_cur.execute("PRAGMA key='" + db_pass + "'")
    db_cur.execute(sql_createTable_Clients)
    db_conn.commit()
    db_cur.execute(sql_createTable_Products)
    db_conn.commit()
    db_cur.execute(sql_createTable_Orders)
    db_conn.commit()
    db_cur.execute(sql_createTable_OrderItems)
    db_conn.commit()
    return db_conn, db_cur

def db_newClient_test(db_conn, db_cur):
    db_cur = db_conn.cursor()    # create cursor object from db connection

    # execute insert into newly created table

    sql_tableInsert_Clients = "INSERT INTO Clients(Id, Name, Address, Phone, Email, DateAdded) values (?,?,?,?,?,?)"
    db_cur.execute("PRAGMA key='password'")
    db_cur.execute(sql_tableInsert_Clients, (1, "Name1", "Address1", "7183497234", "email1", datetime.now()))
    db_conn.commit()
    db_cur.close()


def addNewClient(db_conn, db_cur, name, address1, address2, phone, email):
    """
    Add a new client to the database
    :param db_conn: database connection object
    :param db_cur: database cursor object
    :param name: Client Name to Add
    :param address1: 1st Address Line
    :param address2: 2nd Address Line
    :param phone: Client Phone Number (string)
    :param email: Client email
    :return: boolean whether data was added to db correctly
    """
    # execute insert into newly created table
    try:
        sql_tableInsert_Clients = "INSERT INTO Clients(Name, Address_line1, Address_line2, Phone, Email, DateAdded) values (?,?,?,?,?,?)"
        db_cur.execute(sql_tableInsert_Clients, (name, address1, address2, phone, email, datetime.now()))
        db_conn.commit()
        return 1, "Success!", "Added " + name + " to Client List!"
    except sqlcipher.IntegrityError as e:
        # need to show system dialog to user that name already exists
        e_split = str(e).split()
        if e_split[0] == 'UNIQUE':
            if e_split[3] == 'Clients.Name':
                msg = "Client Name Already Exists!"
        #print(e_split)
        #print("Client Name Already Exists!")
        #ex = sys.exc_info()[0] # exception info
        print(e)
        #print(ex)
        return 0, "Error!", msg

def db_printAllClients(db_conn):
    db_cur = db_conn.cursor()
    db_cur.execute("SELECT * FROM Clients;")
    print(db_cur.fetchall())

def db_printAllProducts(db_conn):
    db_cur = db_conn.cursor()
    db_cur.execute("SELECT * FROM Products;")
    print(db_cur.fetchall())

def db_printAllTables(db_conn):
    db_cur = db_conn.cursor()
    db_cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(db_cur.fetchall())

def db_connectionCheck(db_conn):
    connected = False
    try:
        db_printAllTables(db_conn)
        db_printAllClients(db_conn)
        db_printAllProducts(db_conn)
        connected = True
        return connected
    except:
        return connected
