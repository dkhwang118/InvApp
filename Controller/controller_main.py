###########################################################################
#
#   controller_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   Edited by: David K. Hwang
#
#
############################################################################
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot, QModelIndex
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import webbrowser
import urllib


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
            self._model.productsInCurrentOrder = []
        elif value == 8:
            #print("DEBUG: orders = " + str(self._model.getAllOrders()))
            self._model.pageInit_newInvoiceCandS()

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

    @pyqtSlot(list)
    def currentItemChanged(self, values):
        #print("Selected new item in QTable")
        self._model.prodInOrdrList_selected = True
        for item in values:
            self._model.prodsInOrdrList_selectedIndices = [item.row(), item.column()]
            #print(item.row(), item.column())

    @pyqtSlot(QTableWidgetItem)
    def productAmountChangedInList(self, item):
        if (self._model.prodInOrdrList_selected == False):
            return
        else:
            #get item at selected indices
            #print(item.text())

            # find index
            productIndex = self._model.prodsInOrdrList_selectedIndices[0]

            # change value in list
            self._model.productsInCurrentOrder[productIndex][1] = int(item.text())

            self._model.prodInOrdrList_selected = False
            self._model.updated_ProdInOrderList.emit(self._model.productsInCurrentOrder)

    @pyqtSlot(str, int, str)
    def newOrder_reviewOrder(self, orderNum, clientIndex_inCurCliList, DeliveryDate):
        # gather products and create string
        orderTotal = 0
        products = ""
        for product in self._model.productsInCurrentOrder:
            temp_total = product[0][3] * product[1]
            totalPriceLen = len(str(temp_total))
            ftemp_total = str(temp_total)[:(totalPriceLen - 2)] + "," + str(temp_total)[(totalPriceLen - 2):]
            products += "      " + str(product[0][1]) + " x " + str(product[1]) + " = " + ftemp_total + "\n"
            orderTotal += temp_total

        orderTotalLen = len(str(orderTotal))
        forderTotal = str(orderTotal)[:(orderTotalLen - 2)] + "," + str(orderTotal)[(orderTotalLen - 2):]

        msgText = 'Please Review the Order Below and Select "Yes" if Correct:\n' \
                    + "\n  Order Number: " + orderNum \
                    + "\n  Client Name: " + self._model.currentClientList[clientIndex_inCurCliList][0] \
                    + "\n  Delivery Date: " + DeliveryDate \
                    + "\n  Products In Order: \n" + products \
                    + "\n  Order Sub-Total: " + forderTotal

        reviewOrder_msgBox = QMessageBox.question(self._mainView, "Review and Complete the Order", msgText, QMessageBox.Yes, QMessageBox.No)
        if reviewOrder_msgBox == QMessageBox.Yes:
            # add new order to table, then add products in order
            self._model.addToDB_newOrder(self._model.currentClientList[clientIndex_inCurCliList][1], orderNum, orderTotal, DeliveryDate)
            #print(self._model.getAllOrders())

            # add products to OrderItems table
            for item in self._model.productsInCurrentOrder:
                self._model.addToDB_newOrderItem(item[0][0], self._model.getOrderId_byOrderNum(orderNum), item[1])

            # reset product lists on GUI page
            self._model.productsNotInCurrentOrder = self._model.getAllProducts()
            self._model.productsInCurrentOrder = []
        else:
            # order not finalized. dialog box closes
            #print("other\n")
            return

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
            self._model.getClientInfo_byId_searchEditClients(self._model.currentClientId)

    @pyqtSlot(QModelIndex)
    def searchEditClients_onClientName_doubleClick(self, id):
        """
        Event when a client name in the searchEditClients view list is double-clicked
        :param id: Client Id
        :return:
        """
        self._model.currentClientId = id
        self._model.getClientInfo_byId_searchEditClients(id)
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

    ####################################################################################################################
    #   New Invoice Create and Send page pyqtSlots
    ####################################################################################################################

    @pyqtSlot(QModelIndex)
    def on_newInvoiceCandS_orderSearchListDoubleClick(self, item):
        self._model.pageUpdate_newInvoiceCandS_orderInfo(item)

    @pyqtSlot()
    def on_newInvoiceCandS_showAllOrders_clicked(self):
        self._model.pageUpdate_newInvoiceCandS_allOrdersInList()

    @pyqtSlot()
    def on_newInvoiceCandS_showAllUnsentOrders_clicked(self):
        self._model.pageUpdate_newInvoiceCandS_allUnsentOrdersInList()

    @pyqtSlot(str, str)
    def on_newInvoiceCandS_taxValueChanged(self, taxValue, subTotal):
        if (taxValue == ""):
            #do nothing
            return
        else:
            # convert taxValue from string to float
            fTaxValue = 0.0
            float_taxValue = 0.0
            if (taxValue.find(',') != -1):
                fTaxValue = taxValue.replace(',', '.')
            else:
                fTaxValue = taxValue
            float_taxValue = float(fTaxValue)

            #print("CONTROLLER_DEBUG: taxValue=" + str(float_taxValue))

            # format subtotal from string to int
            fSubTotal = 0
            # if "," or "." found => delete
            if (subTotal.find(',') != -1):
                fSubTotal = subTotal.replace(',', '.')
            else:
                fSubTotal = subTotal
            float_subTotal = float(fSubTotal)

            #print("CONTROLLER_DEBUG: orderSubTotal=" + str(float_subTotal))
            # calc total w/ above values
            orderTotal = float_subTotal + (float_subTotal * (float_taxValue / 100))
            #print("CONTROLLER_DEBUG: orderTotal=" + str(orderTotal))

            # format orderTotal
            # find where decimal is
            decIndex = str(orderTotal).find('.')
            #print("CONTROLLER_DEBUG: decIndex=" + str(decIndex))

            fOrderTotal = ""
            string_orderTotal = str(orderTotal)
            # cut-off tail and round up if necessary
            digitsAfterDecimalPoint = len(string_orderTotal) - (decIndex+1)
            if digitsAfterDecimalPoint > 2:
                fOrderTotal = string_orderTotal[:(decIndex + 3)]
                if (int(string_orderTotal[(decIndex+3)]) > 5 ):
                    fOrderTotal = str(float(fOrderTotal) + 0.01)
            elif digitsAfterDecimalPoint == 1:
                fOrderTotal = string_orderTotal + "0"
            elif digitsAfterDecimalPoint == -1:
                fOrderTotal = string_orderTotal + ".00"

            orderTotalLen = len(str(fOrderTotal))
            # if for some reason it still isn't cut off
            decIndex = fOrderTotal.find('.')
            if ((len(str(fOrderTotal)) - decIndex) != 2):
                fOrderTotal = fOrderTotal[:(decIndex+3)]

            #fOrderTotal = str(orderTotal)[:(orderTotalLen - 2)] + "," + str(orderTotal)[(orderTotalLen - 2):]
            #print("CONTROLLER_DEBUG: orderTotal2=" + str(fOrderTotal))
            self._model.updated_orderTotal.emit(fOrderTotal)

    pyqtSlot(str, str, str, str)
    def send_invoiceData_toBrowser(self, orderNum, subtotal, tax, total):
        orderId = self._model.getOrderId_byOrderNum(orderNum)

        # get all order info from orderId
        # print("got order id " + orderId.text() + ", now make model display order values")
        templist0 = self._model.getOrderData_byFullOrderNum(orderNum)
        #print("CONT_DEBUG: templist0=" + str(templist0))

        # get client info from orderId
        # print(str(self.getClientInfo_byId(templist0[0])))
        templist1 = self._model.getClientInfo_byId(templist0[0])
        #print("CONT_DEBUG: templist1=" + str(templist1))

        # get product info and format info for display
        templist2 = self._model.getAllOrderItemData_byOrderId(orderId)
        #print("CONT_DEBUG: templist2=" + str(templist2))

        # add invoice to invoices db table
        self._model.addToDB_newInvoice_singleOrder(templist0[1], templist0[0], orderId)

        # reset GUI values
        self._model.pageInit_newInvoiceCandS()

        # code/idea for generic mailto: template credit goes to "Fabio" @: https://stackoverflow.com/a/39269802
        myOrg = "MyVeryOwnBusiness"
        recipient = templist1[4]
        subject = "Invoice for Recent Order from " + myOrg
        products = ""
        for (pId, pName, priceInCents, numInOrder) in templist2:
            itemPrice = self._model.convert_itemPrice(priceInCents)
            itemTotalPrice = self._model.convert_itemPrice(priceInCents * numInOrder)
            products += "" + pName + ": " + itemPrice + " x " + str(numInOrder) + " = " + itemTotalPrice + "%0D%0A"


        temp_TaxTotal = str(float(total) - float(subtotal))
        decIndex = temp_TaxTotal.find('.')
        fTaxTotal = ""

        digitsAfterDecimalPoint = len(temp_TaxTotal) - (decIndex+1)
        if digitsAfterDecimalPoint > 2:
            fTaxTotal = temp_TaxTotal[:(decIndex + 3)]
            if (int(temp_TaxTotal[(decIndex+3)]) > 5 ):
                fTaxTotal = str(float(fTaxTotal) + 0.01)
                decIndex = fTaxTotal.find('.')
                temp_digitsAfterDecimalPoint = len(fTaxTotal) - (decIndex + 1)
                if (temp_digitsAfterDecimalPoint == 1):
                    # round-up changed the digit infront of the one being edited => must add a '0' to the end
                    fTaxTotal = fTaxTotal + "0"
        elif digitsAfterDecimalPoint == 1:
            fTaxTotal = temp_TaxTotal + "0"
        elif digitsAfterDecimalPoint == -1:
            fTaxTotal = temp_TaxTotal + ".00"

        #print("MAIL_DEBUG: temp_taxTotal=" + fTaxTotal)
        # if for some reason it still isn't cut off
        decIndex = fTaxTotal.find('.')
        if ((len(str(fTaxTotal)) - decIndex) != 2):
            fTaxTotal = fTaxTotal[:(decIndex+3)]

        #print("MAIL_DEBUG2: temp_taxTotal=" + fTaxTotal)

        # newline code idea from "cyang" @: https://stackoverflow.com/a/10356432
        body = "From " + myOrg + "%0D%0A%0D%0A%0D%0A" \
            + "ORDER " + templist0[1] + "%0D%0A%0D%0A" \
            + products + "%0D%0A" \
            + "Subtotal: $" + subtotal + "%0D%0A" \
            + "Tax (" + tax + "%): $" + fTaxTotal + "%0D%0A" \
            + "Total Amount Owed: $" + total + "\n\n\n"

        body = body.replace(' ', '%20')         # replace whitespace with url encoded whitespace
        body = body.replace('\n', '%0D%0A')     # same for newlines
        #browser_controller = webbrowser.get("google-chrome")
        webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)




