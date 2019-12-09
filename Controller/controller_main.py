###########################################################################
#
#   controller_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   Edited by: David K. Hwang
#
#
############################################################################

from PyQt5.QtCore import QObject, pyqtSlot, QModelIndex
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QMessageBox


class MainController(QObject):
    # class variables
    _mainView = None        # placeholder for the MainView window
    _startupView = None     # placeholder for the StartupView window
    _incorrectPass = None

    def __init__(self, model):
        super().__init__()

        self._model = model
        self._self = self

    def define_mainView(self, qObj):
        self._mainView = qObj

    def define_startupView(self, qObj):
        self._startupView = qObj

    def define_passDialog(self, qObj):
        self._incorrectPass = qObj

    ######################################################
    #   MainWindow functions and pyqtSlots
    ######################################################
    # pyqtSlot and function to handle tier1 (leftmost) button clicks
    @pyqtSlot(int)
    def buttonClick_tier1(self, value):
        if self._model.currentTier2Buttons == value:
            self._model.currentTier2Buttons = 0
        else:
            self._model.currentTier2Buttons = value

    @pyqtSlot()
    def buttonClick_passDialog(self):
        self._incorrectPass.on_buttonClick_ok()

    @pyqtSlot(int)
    def change_mainView(self, value):
        self._model.currentView = value
        if value == 1:  # if new view is newOrders => tell model to get relevant data
            self._model.currentClientList = self._model.getAllClients()
            self._model.productsNotInCurrentOrder = self._model.getAllProducts()

    @pyqtSlot(str)
    def buttonClick_passwordLogin(self, value):
        # code to tell controller to attempt db connection with given password value
        connected = self._model.db_connection_init(value)

        if connected:
            # after successful connection, show mainview
            self._startupView.hide()
            self._mainView.show()
        else:
            self._incorrectPass.show()

    ####################################################################################################################
    #   newOrder page pyqtSlots
    ####################################################################################################################
    @pyqtSlot(int)
    def addProd_toNewOrder(self, index):
        # get product from productsNotInCurrentOrder using index of currently selected item(s)
        self._model.newOrder_addProdToOrder(index)

    @pyqtSlot(int)
    def removeProd_fromNewOrder(self, index):
        self._model.newOrder_removeProdFromOrder(index)

    @pyqtSlot()
    def currentItemChanged(self):
        print("edited current item in QTable\n")

    @pyqtSlot(str, int, str)
    def newOrder_reviewOrder(self, orderNum, clientIndex_inCurCliList, orderDate):
        # gather products and create string
        products = ""
        #for (pId, pName, pDesc, priceInCents, dateAdded) in self._model.productsInCurrentOrder:
        #    products +=

        msgText = """Please Review the Order Below and Select "Yes" if Correct:\n
                    Order Number: """ + orderNum + """\n
                    Client Name: """ + self._model.currentClientList[clientIndex_inCurCliList][0] + """\n
                    Order Date: """ + orderDate + """\n
                    Products: """

        reviewOrder_msgBox = QMessageBox.question(self._mainView, "Review and Complete the Order", msgText, QMessageBox.Yes, QMessageBox.No)
        if reviewOrder_msgBox == QMessageBox.Yes:
            print("pressed yes\n")
        else:
            print("other\n")


    ####################################################################################################################
    #   addNewClient page pyqtSlots
    ####################################################################################################################

    @pyqtSlot(str, str, str, str, str)
    def cntrl_addNewClient(self, name, address1, address2, phone, email):
        return_val, title, text = self._model.db_addNewClient(name, address1, address2, phone, email)
        self._model.message_box_values = (title, text)
        self._model.last_db_return_value = return_val

    ####################################################################################################################
    #   searchEditClients page pyqtSlots
    ####################################################################################################################

    def searchClientNames_byName(self, currentNameText):
        if currentNameText == "":
            self._model.getAllClients()
        else:
            self._model.getAllClients_byName(currentNameText)

    @pyqtSlot()
    def searchEditClients_enableEditInfo_buttonClick(self):
        if self._model.searchEditClients_editMode == 0:
            self._model.searchEditClients_editMode = 1
        else:
            self._model.searchEditClients_editMode = 0
            self._model.getClientInfo_byId(self._model.currentClientId)

    @pyqtSlot(QModelIndex)
    def searchEditClients_onClientName_doubleClick(self, id):
        """
        Event when a client name in the searchEditClients view list is double-clicked
        :param id: Client Id
        :return:
        """
        self._model.currentClientId = id
        self._model.getClientInfo_byId(id)
        return

    @pyqtSlot(str, str, str, str, str)
    def searchEditClients_finalizeInfo_buttonClick(self, name, address1, address2, phone, email):
        self._model.editClientInfo_byCurrentId(name, address1, address2, phone, email)

    ####################################################################################################################
    #   newProduct page pyqtSlots
    ####################################################################################################################

    @pyqtSlot(str, str, str)
    def newProduct_addProduct_buttonClick(self, name, description, priceInCents):
        fPriceInCents = 0
        # if "," or "." found => delete
        if (priceInCents.find(',') != -1):
            fPriceInCents = int(priceInCents.replace(',', ''))
        elif (priceInCents.find('.') != -1):
            fPriceInCents = int(priceInCents.replace('.', ''))
        self._model.addNewProduct(name, description, fPriceInCents)
