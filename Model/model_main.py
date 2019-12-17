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
from PyQt5.QtGui import QStandardItemModel, QStandardItem
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
    updated_ProdInOrderListIndices = pyqtSignal(int, int)
    updated_newOrderNum = pyqtSignal(int)
    addNewOrderSuccess_newOrderNum = pyqtSignal(str)

    # singals for newInvoice page
    updated_newInvoice_clientList = pyqtSignal(list)

    # define models for temp data storage (per-page)
    model_listView_newInvoiceCandS_orderList = QStandardItemModel()
    model_listView_newInvoiceCandS_orderItems = QStandardItemModel()
    updated_orderList = pyqtSignal(QStandardItemModel)
    updated_orderData = pyqtSignal(str, str, str, str, str, str, int)
    updated_orderTotal = pyqtSignal(str)


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

    @property
    def prodsInOrdrList_selectedIndices(self):
        return self._prodsInOrdrList_selectedIndices

    @prodsInOrdrList_selectedIndices.setter
    def prodsInOrdrList_selectedIndices(self, value):
        self._prodsInOrdrList_selectedIndices = value
        #self.updated_ProdInOrderListIndices.emit(x, y)

    @property
    def prodInOrdrList_selected(self):
        return self._prodInOrdrList_selected

    @prodInOrdrList_selected.setter
    def prodInOrdrList_selected(self, value):
        self._prodInOrdrList_selected = value

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

    ####################################################################################################################
    #   Create and Send Invoice properties
    ####################################################################################################################

    @property
    def model_listView_newInvoiceCandS_orderList(self):
        return self._model_listView_newInvoiceCandS_orderList

    @model_listView_newInvoiceCandS_orderList.setter
    def model_listView_newInvoiceCandS_orderList(self, values):
        self._model_listView_newInvoiceCandS_orderList = values
        self.updated_orderList.emit(values)

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
        self.prodsInOrdrList_selectedIndices = [-1, -1]
        self._prodInOrdrList_selected = False

        # Create and Send invoice model
        self._model_listView_newInvoiceCandS_orderList = QStandardItemModel()
        self.model_listView_newInvoiceCandS_orderItems = QStandardItemModel()

        self.newOrder_productAmtDict = {}

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
        #db_printAllClients(self._db_connection)
        return return_val, title, text

    def getAllClients(self):
        db_cur = self._db_connection.cursor()
        db_cur.execute("SELECT Name, Id FROM Clients;")
        clientNameList = db_cur.fetchall()
        if (self._currentView == 4):
            self.searchEditClients_searchClientNames_newValues.emit(clientNameList)
        elif (self._currentView == 7):
            self.updated_newInvoice_clientList.emit(clientNameList)
        return clientNameList

    def getAllClients_byName(self, name):
        db_cur = self._db_connection.cursor()
        formattedName = name + "%"
        db_cur.execute("SELECT Name, Id FROM Clients WHERE Name LIKE ?;", (formattedName,))
        if (self._currentView == 4):
            self.searchEditClients_searchClientNames_newValues.emit(db_cur.fetchall())
        elif (self._currentView == 7):
            self.updated_newInvoice_clientList.emit(db_cur.fetchall())

    def getClientInfo_byId(self, id):
        db_cur = self._db_connection.cursor()
        db_cur.execute("SELECT * FROM Clients WHERE Id=?;", (str(id),))
        return db_cur.fetchone()[1:]

    def getClientInfo_byId_searchEditClients(self, id):
        db_cur = self._db_connection.cursor()
        db_cur.execute("SELECT * FROM Clients WHERE Id=?;", (str(id),))
        tempList = db_cur.fetchone()
        #print(tempList)
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
            print(str(e))
            e_split = str(e).split()
            if e_split[0] == 'UNIQUE':
                if e_split[3] == 'Products.Name':
                    msg = "Product Name Already Exists! Please use a UNIQUE name for each Product!"
            self.show_message_box.emit(("Add Product Failed!", msg))

    def addToDB_newOrder(self, clientId, orderNum, subTotal, deliveryDate = "NotSet", orderPaid = 0, orderPaidDate = "NotPaid"):
        try:
            db_cur = self._db_connection.cursor()
            sql_tableInsert_Orders = """INSERT INTO Orders(ClientId, FullOrderNumber, OrderYear, 
                                                        OrderMonth, OrderNumber, DeliveryDate, 
                                                        SubTotal, OrderPaid, CreatedDate) values (?,?,?,?,?,?,?,?,?)"""
            fDeliveryDate = ""
            if (deliveryDate == ""): fDeliveryDate = "NotSet"
            else: fDeliveryDate = deliveryDate
            db_cur.execute(sql_tableInsert_Orders, (clientId, orderNum, orderNum[:2],
                                                    orderNum[2:4], orderNum[4:], fDeliveryDate,
                                                    subTotal, orderPaid, datetime.now()))
            self._db_connection.commit()
            self.addNewOrderSuccess_newOrderNum.emit(self.getNextOrderNum())
            #text = "Product \"" + name + "\" Successfully Added to Database!"
            #self.show_message_box.emit(("Add New Product Success!", text))
        except sqlcipher.IntegrityError as e:
            #print(e)
            msg = str(e)
            e_split = str(e).split()
            if e_split[0] == 'UNIQUE':
                if e_split[3] == 'Orders.FullOrderNumber':
                    msg = "Order Number Already Exists! Please use a UNIQUE number for each Order Number!\n" \
                            + "Next Available Order Number: " + self.getNextOrderNum()
            self.show_message_box.emit(("Create Order Failed!", msg))

    def addToDB_newOrderItem(self, pId, orderId, numInOrder):
        try:
            db_cur = self._db_connection.cursor()
            sql_tableInsert_OrderItem = """INSERT INTO OrderItems(ProductId, OrderId, NumInOrder) values (?,?,?)"""
            db_cur.execute(sql_tableInsert_OrderItem, (int(pId), int(orderId), int(numInOrder)))
            self._db_connection.commit()
            #text = "Product \"" + name + "\" Successfully Added to Database!"
            #self.show_message_box.emit(("Add New Product Success!", text))
        except sqlcipher.IntegrityError as e:
            print(str(e))
            e_split = str(e).split()
            if e_split[0] == 'UNIQUE':
                if e_split[3] == 'OrderItems.ProductId':
                    msg = "Order Number Already Exists! Please use a UNIQUE number for each Order Number!\n"
            self.show_message_box.emit(("Create Order Failed!", str(e)))

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
            #print(self.getAllOrders())
            db_cur.execute("""SELECT OrderNumber 
                            FROM Orders 
                            WHERE OrderYear = ?
                            AND OrderMonth = ?;""", (int(year),int(month)))
            orderNumList = db_cur.fetchall()
            #print(orderNumList)
            # find largest value given list of tuples
            fOrderNumList = []
            for order in orderNumList:
                fOrderNumList.append(order[0])

            if not orderNumList:    # if order list is empty
                orderNum = year + month + "001"     # order is first of the month
            else:   # find last order number in list
                newOrderNum = (max(fOrderNumList) + 1)
                fNewOrderNum = ""
                if len(str(newOrderNum)) == 1:
                    fNewOrderNum = "00" + str(newOrderNum)
                elif len(str(newOrderNum)) == 2:
                    fNewOrderNum = "0" + str(newOrderNum)
                else:
                    fNewOrderNum = str(newOrderNum)
                orderNum = year + month + fNewOrderNum
            return orderNum
        except sqlcipher.IntegrityError as e:
            print(str(e))
            self.show_message_box.emit("getNextOrderNum Error", str(e))

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

    def newOrder_getAllProducts(self):
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
        if (len(self.productsNotInCurrentOrder) > 0):
            addedProduct = self._productsNotInCurrentOrder.pop(index)                   # get prod from first list
            self.updated_ProdNotInOrderList.emit(self._productsNotInCurrentOrder)       # emit signal to update first list
            productId = addedProduct[0]
            self.newOrder_productAmtDict[productId] = 1
            self._productsInCurrentOrder.append([addedProduct, 1])
            self.updated_ProdInOrderList.emit(self._productsInCurrentOrder)

    def newOrder_removeProdFromOrder(self, index):
        if (len(self.productsInCurrentOrder) > 0):
            removedProduct = self._productsInCurrentOrder.pop(index)
            self.updated_ProdInOrderList.emit(self._productsInCurrentOrder)
            productId = removedProduct[0]
            self.newOrder_productAmtDict[productId] = 0
            self._productsNotInCurrentOrder.append(removedProduct[0])
            self.updated_ProdNotInOrderList.emit(self._productsNotInCurrentOrder)

    def getAllOrders(self):
        try:
            db_cur = self._db_connection.cursor()
            db_cur.execute("""SELECT * FROM Orders;""")
            orderList = db_cur.fetchall()
            return orderList
        except:
            ex = sys.exc_info()[0] # exception info
            print(ex)
            return []

    def getOrderData_byFullOrderNum(self, value):
        try:
            db_cur = self._db_connection.cursor()
            db_cur.execute("""SELECT * 
                            FROM Orders 
                            WHERE FullOrderNumber = ?;""", (value,))
            return db_cur.fetchone()[1:]
        except:
            ex = sys.exc_info()[0] # exception info
            print(ex)
            return -1

    def getOrderId_byOrderNum(self, orderNum):
        try:
            db_cur = self._db_connection.cursor()
            db_cur.execute("""SELECT Id 
                            FROM Orders 
                            WHERE FullOrderNumber = ?;""", (str(orderNum),))
            orderId = db_cur.fetchone()
            return orderId[0]
        except:
            ex = sys.exc_info()[0] # exception info
            print(ex)
            return -1

    def getAllOrderItems_byOrderId(self, orderId):
        try:
            db_cur = self._db_connection.cursor()
            db_cur.execute("""SELECT * 
                            FROM OrderItems 
                            WHERE OrderId = ?;""", (int(orderId),))
            orderItemsList = db_cur.fetchall()
            return orderItemsList
        except:
            ex = sys.exc_info()[0] # exception info
            print(ex)
            return []

    def getAllOrderItemData_byOrderId(self, orderId):
        try:
            db_cur = self._db_connection.cursor()
            db_cur.execute("""SELECT prods.Id, prods.Name, prods.PriceInCents, prods.NumInOrder
                            FROM (
                                SELECT Id, OrderId, Name, PriceInCents, NumInOrder
                                FROM Products
                                INNER JOIN OrderItems
                                    ON OrderItems.ProductId = Products.Id
                                WHERE Id IN (
                                    SELECT ProductId 
                                    FROM OrderItems 
                                    WHERE OrderId = ?)
                                ) AS prods
                            WHERE prods.OrderId = ?;""", (int(orderId),int(orderId)))
            orderItemsList = db_cur.fetchall()
            return orderItemsList
        except:
            ex = sys.exc_info()[0] # exception info
            print(ex)
            return []

    def addToDB_newInvoice_singleOrder(self, invoiceNum, clientId, orderId, numOrders = 1):
        try:
            db_cur = self._db_connection.cursor()
            sql_tableInsert_Invoices = """INSERT INTO Invoices(InvoiceNum, ClientId, NumOrders, InvoiceSent) values (?,?,?,?)"""
            sql_tableInsert_InvoiceOrder = """INSERT INTO InvoiceOrders(InvoiceId, OrderId) values (?,?)"""

            # insert into invoices to generate invoice id
            db_cur.execute(sql_tableInsert_Invoices, (str(invoiceNum), int(clientId), int(numOrders), 1))
            self._db_connection.commit()

            # search for invoice id that matches invoiceNum
            db_cur.execute("""SELECT Id
                            FROM Invoices
                            WHERE InvoiceNum = ?;""", (str(invoiceNum),))
            invoiceId = db_cur.fetchone()
            #print(invoiceId)

            db_cur.execute(sql_tableInsert_InvoiceOrder, (int(invoiceId[0]), int(orderId)))
            self._db_connection.commit()
            #text = "Product \"" + name + "\" Successfully Added to Database!"
            #self.show_message_box.emit(("Add New Product Success!", text))
        except sqlcipher.IntegrityError as e:
            #print(str(e))
            self.show_message_box.emit(("Create/Send Invoice Failed!", str(e)))

    def getAllUnsentInvoiceOrders(self):
        try:
            db_cur = self._db_connection.cursor()
            db_cur.execute("""SELECT *
                            FROM Orders
                            WHERE FullOrderNumber NOT IN (         
                                SELECT InvoiceNum 
                                FROM Invoices
                                WHERE InvoiceSent = 1);""")
            orderList = db_cur.fetchall()
            return orderList
        except:
            ex = sys.exc_info()[0] # exception info
            print(ex)
            return []


    ########################################
    #   pageInit Calls
    ########################################

    def pageInit_newInvoiceCandS(self):
        self._model_listView_newInvoiceCandS_orderList.clear()
        for orderRow in self.getAllUnsentInvoiceOrders():
            self._model_listView_newInvoiceCandS_orderList.appendRow(QStandardItem(orderRow[2]))
        self.updated_orderList.emit(self._model_listView_newInvoiceCandS_orderList)

    ########################################
    #   pageUpdate Calls
    ########################################

    def pageUpdate_newInvoiceCandS_allOrdersInList(self):
        self._model_listView_newInvoiceCandS_orderList.clear()
        for orderRow in self.getAllOrders():
            self._model_listView_newInvoiceCandS_orderList.appendRow(QStandardItem(orderRow[2]))
        self.updated_orderList.emit(self._model_listView_newInvoiceCandS_orderList)

    def pageUpdate_newInvoiceCandS_allUnsentOrdersInList(self):
        self._model_listView_newInvoiceCandS_orderList.clear()
        for orderRow in self.getAllUnsentInvoiceOrders():
            self._model_listView_newInvoiceCandS_orderList.appendRow(QStandardItem(orderRow[2]))
        self.updated_orderList.emit(self._model_listView_newInvoiceCandS_orderList)

    def convert_itemPrice(self, priceInCents):
        priceLen = len(str(priceInCents))
        return str(priceInCents)[:(priceLen - 2)] + "," + str(priceInCents)[(priceLen - 2):]

    def pageUpdate_newInvoiceCandS_orderInfo(self, item):
        # get the full order number QItem from the ListView's QModelIndex object
        orderNumItem = self.model_listView_newInvoiceCandS_orderList.item(item.row())

        # get the orderId from the full order number
        orderId = self.getOrderId_byOrderNum(orderNumItem.text())

        # get all order info from orderId
        templist0 = self.getOrderData_byFullOrderNum(orderNumItem.text())

        # get client info from clientId
        templist1 = self.getClientInfo_byId(templist0[0])

        # get product info and format info for display
        templist2 = self.getAllOrderItemData_byOrderId(orderId)

        # clear items in OrderProducts model and append new items from order data to model
        self.model_listView_newInvoiceCandS_orderItems.clear()
        for (pId, pName, priceInCents, numInOrder) in templist2:
            itemPrice = self.convert_itemPrice(priceInCents)
            itemTotalPrice = self.convert_itemPrice(priceInCents * numInOrder)
            self.model_listView_newInvoiceCandS_orderItems.appendRow(QStandardItem("" + pName + ": " + itemPrice + " x " + str(numInOrder) + " = " + itemTotalPrice))

        # emit signal to GUI to update lineEdit texts with order and client data
        self.updated_orderData.emit(templist1[0],
                                templist1[1],
                                templist1[2],
                                templist1[3],
                                templist1[4],
                                templist0[1],
                                templist0[6])