###########################################################################
#
#   model_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   sqlite3 implementation framework by "Adam McQuistan" (https://stackabuse.com/a-sqlite-tutorial-with-python/)
#
#   Edited by: David K. Hwang
#
#
############################################################################

from PyQt5.QtCore import QObject, pyqtSignal
from Model.model_sql_db_utils import *


class Model(QObject):

    # define signals dependent on changes in model
    amount_changed = pyqtSignal(int)
    even_odd_changed = pyqtSignal(str)
    enable_reset_changed = pyqtSignal(bool)

    # define page-change signal
    mainView_changed = pyqtSignal(int)
    currentTier2Buttons_changed = pyqtSignal(int)

    # signal to tell view to show a QMessageBox with given string values (title, text)
    show_message_box = pyqtSignal(tuple)

    # signal to tell view whether last call was successful or not
    call_success = pyqtSignal(int)

    # signal to tell view about updated list values
    searchEditClients_searchClientNames_newValues = pyqtSignal(list)
    searchEditClients_clientInfoDoubleClick = pyqtSignal(str, str, str, str, str)

    # signal to tell view about changes in modes depedning on button press
    searchEditClients_editModeChanged = pyqtSignal(int)

    # signals for newOrder page
    # signal for updated client list (Name, Id)
    updatedClientList_NameId = pyqtSignal(list)
    updated_ProdNotInOrderList = pyqtSignal(list)
    updated_ProdInOrderList = pyqtSignal(list)
    updated_ProdAmountsInOrderList = pyqtSignal(list)


    ####################################################################################################################
    #   MainWindow properties
    ####################################################################################################################

    @property
    def currentView(self):
        return self._currentView

    @currentView.setter
    def currentView(self, value):
        self._currentView = value
        self.mainView_changed.emit(value)

    @property
    def currentTier2Buttons(self):
        return self._currentTier2Buttons

    @currentTier2Buttons.setter
    def currentTier2Buttons(self, value):
        self._currentTier2Buttons = value
        self.currentTier2Buttons_changed.emit(value)

    @property
    def message_box_values(self):
        return self._message_box_values

    @message_box_values.setter
    def message_box_values(self, value):
        self._message_box_values = value
        self.show_message_box.emit(value)

    @property
    def last_db_return_value(self):
        return self._last_db_return_value

    @last_db_return_value.setter
    def last_db_return_value(self, value):
        self._last_db_return_value = value
        self.call_success.emit(value)

    @property
    def firstTimeStartup(self):
        return self._firstTimeStartup

    @property
    def db_connection(self):
        return self._db_connection

    @db_connection.setter
    def db_connection(self, db_conn):
        self._db_connection = db_conn

    @property
    def db_cursor(self):
        return self._db_connection

    @db_cursor.setter
    def db_cursor(self, db_cur):
        self._db_cursor = db_cur

    ####################################################################################################################
    #   newOrder properties
    ####################################################################################################################

    @property
    def nextOrderNumber(self):
        return self._nextOrderNumber

    @nextOrderNumber.setter
    def nextOrderNumber(self, value):
        self._nextOrderNumber = value

    @property
    def currentClientList(self):
        return self._currentClientList

    @currentClientList.setter
    def currentClientList(self, values):
        self._currentClientList = values
        self.updatedClientList_NameId.emit(values)

    @property
    def currentDate(self):
        return self._currentDate

    @property
    def productsNotInCurrentOrder(self):
        return self._productsNotInCurrentOrder

    @productsNotInCurrentOrder.setter
    def productsNotInCurrentOrder(self, values):
        self._productsNotInCurrentOrder = values
        self.updated_ProdNotInOrderList.emit(values)

    @property
    def productsInCurrentOrder(self):
        return self._productsInCurrentOrder

    @productsInCurrentOrder.setter
    def productsInCurrentOrder(self, values):
        self._productsInCurrentOrder = values
        self.updated_ProdInOrderList.emit(values)

    @property
    def productAmountsInCurrentOrder(self):
        return self._productAmountsInCurrentOrder

    @productAmountsInCurrentOrder.setter
    def productAmountsInCurrentOrder(self, values):
        self._productAmountsInCurrentOrder = values
        self.updated_ProdAmountsInOrderList.emit(values)

    ####################################################################################################################
    #   SearchEditClients properties
    ####################################################################################################################

    @property
    def searchEditClients_editMode(self):
        return self._searchEditClients_editMode

    @searchEditClients_editMode.setter
    def searchEditClients_editMode(self, value):
        self._searchEditClients_editMode = value
        self.searchEditClients_editModeChanged.emit(value)

    @property
    def currentClientId(self):
        return self._currentClientId

    @currentClientId.setter
    def currentClientId(self, value):
        self._currentClientId = value

#######################################################################
#
#   INITIALIZATION
#
#######################################################################

    def __init__(self):
        super().__init__()

        # on model init, check if database file exists
        if db_isPresent():
            self._firstTimeStartup = False
        else:
            self._firstTimeStartup = True

        # init _db_connection
        self._db_connection = None
        self._db_cursor = None

        # set current view for main window
        self._currentView = 0

        # set current visibility of Tier2 buttons
        self._currentTier2Buttons = 0

        self._message_box_values = ("", "")
        self._last_db_return_value = -1

        # set searchEditClient page signals and properties
        self._searchEditClients_editMode = 0

        # misc global propertes
        self._currentClientId = -1
        self._currentOrderNumber = 0
        self._nextOrderNumber = "0000001"
        self._currentClientList = []
        self._currentDate = self.getCurrentDate()

        # newOrder page properties
        self._productsNotInCurrentOrder = []
        self._productsInCurrentOrder = []
        self._productAmountsInCurrentOrder = []

    #######################################################################
    #
    #   Database functions to query and change data
    #
    #######################################################################

    # function to try given password
    def db_connection_init(self, db_pass):
        # start db connection based on if initial application launch or re-login
        if self._firstTimeStartup:
            self._db_connection, self._db_cursor = firstTimeCreate(db_pass)
        else:
            self._db_connection, self._db_cursor = create_connection(db_pass)

        # check to see if password was correct (if app is connected to db) and return boolean result
        return db_connectionCheck(self._db_connection)

    def getCurrentDate(self):
        fullDate = str(datetime.now())
        date = fullDate.split()
        date_split = date[0].split('-')
        fullYear = date_split[0]
        year = fullYear[2:]
        month = date_split[1]
        day = date_split[2]
        return fullYear + "-" + month + "-" + day

    ### function to add new clients to db
    def db_addNewClient(self, name, address1, address2, phone, email):
        return_val, title, text = addNewClient(self._db_connection, self._db_cursor, name, address1, address2, phone, email)
        db_printAllClients(self._db_connection)
        return return_val, title, text

    def getAllClients(self):
        db_cur = self._db_connection.cursor()
        db_cur.execute("SELECT Name, Id FROM Clients;")
        clientNameList = db_cur.fetchall()
        self.searchEditClients_searchClientNames_newValues.emit(clientNameList)
        return clientNameList

    def getAllClients_byName(self, name):
        db_cur = self._db_connection.cursor()
        formattedName = name + "%"
        db_cur.execute("SELECT Name, Id FROM Clients WHERE Name LIKE ?;", (formattedName,))
        self.searchEditClients_searchClientNames_newValues.emit(db_cur.fetchall())

    def getClientInfo_byId(self, id):
        db_cur = self._db_connection.cursor()
        db_cur.execute("SELECT * FROM Clients WHERE Id=?;", (str(id),))
        tempList = db_cur.fetchone()
        print(tempList)
        name = tempList[1]
        address1 = tempList[2]
        address2 = tempList[3]
        phone = tempList[4]
        email = tempList[5]
        self.searchEditClients_clientInfoDoubleClick.emit(name, address1, address2, phone, email)

    def editClientInfo_byCurrentId(self, name, address1, address2, phone, email):
        db_cur = self._db_connection.cursor()
        update = """UPDATE Clients
                    SET Name = ?,
                        Address_line1 = ?,
                        Address_line2 = ?,
                        Phone = ?,
                        Email = ?
                    WHERE Id = ?"""
        try:
            db_cur.execute(update, (name, address1, address2, phone, email, self._currentClientId))
            self._db_connection.commit()
            text = "Client \"" + name + "\" Information Edit Successful."
            #self.searchEditClients_searchClientNames_newValues     code would be here to emit signal to refresh client names in listview
            self.show_message_box.emit(("Edit Client Information Success!", text))
            self.searchEditClients_editModeChanged.emit(0)
        except sqlcipher.IntegrityError as e:
            #print(e)
            e_split = str(e).split()
            if e_split[0] == 'UNIQUE':
                if e_split[3] == 'Clients.Name':
                    msg = "Client Name Already Exists! Please use a UNIQUE name for each client!"
            self.show_message_box.emit(("Edit Client Information Failed!", msg))

    def addNewProduct(self, name, description, priceInCents):
        try:
            db_cur = self._db_connection.cursor()
            sql_tableInsert_Products = "INSERT INTO Products(Name, Description, PriceInCents, DateAdded) values (?,?,?,?)"
            db_cur.execute(sql_tableInsert_Products, (name, description, priceInCents, datetime.now()))
            self._db_connection.commit()
            text = "Product \"" + name + "\" Successfully Added to Database!"
            self.show_message_box.emit(("Add New Product Success!", text))
        except sqlcipher.IntegrityError as e:
            print(e)
            e_split = str(e).split()
            if e_split[0] == 'UNIQUE':
                if e_split[3] == 'Products.Name':
                    msg = "Product Name Already Exists! Please use a UNIQUE name for each Product!"
            self.show_message_box.emit(("Add Product Failed!", msg))

    def getNextOrderNum(self):
        try:
            db_cur = self._db_connection.cursor()
            # get and parse current date
            temp = str(datetime.now())
            date = temp.split()
            date_split = date[0].split('-')
            fullYear = date_split[0]
            year = fullYear[2:]
            month = date_split[1]
            day = date_split[2]

            db_cur.execute("""SELECT OrderNumber 
                            FROM Orders 
                            WHERE OrderYear = ?
                            AND OrderMonth = ?;""", (year,month))
            orderNumList = db_cur.fetchall()
            print(orderNumList)
            if not orderNumList:    # if order list is empty
                orderNum = year + month + "001"
            else:   # find last order number in list
                orderNum = year + month + str(max(orderNumList))
            return orderNum
        except sqlcipher.IntegrityError as e:
            print(e)
            self.show_message_box.emit("getNextOrderNum Error", e)

    def getAllProducts(self):
        try:
            db_cur = self._db_connection.cursor()
            db_cur.execute("""SELECT * FROM Products;""")
            prodList = db_cur.fetchall()
            return prodList
        except:
            ex = sys.exc_info()[0] # exception info
            print(ex)
            return []

    def newOrder_addProdToOrder(self, index):
        addedProduct = self._productsNotInCurrentOrder.pop(index)
        self.updated_ProdNotInOrderList.emit(self._productsNotInCurrentOrder)
        self._productsInCurrentOrder.append(addedProduct)
        self.updated_ProdInOrderList.emit(self._productsInCurrentOrder)

    def newOrder_removeProdFromOrder(self, index):
        removedProduct = self._productsInCurrentOrder.pop(index)
        self.updated_ProdInOrderList.emit(self._productsInCurrentOrder)
        self._productsNotInCurrentOrder.append(removedProduct)
        self.updated_ProdNotInOrderList.emit(self._productsNotInCurrentOrder)
