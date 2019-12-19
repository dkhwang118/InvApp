###########################################################################
#
#   view_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   Edited by: David K. Hwang
#
#
#   pyuic5 Views\view_main_ui.ui -o Views\view_main_ui.py
#
#   to convert .ui to .py
#
############################################################################

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Views.view_main_layout import Ui_MainWindow_mainView


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model                         # connect App to MainView
        self._main_controller = main_controller     # connect cntrl
        self._ui = Ui_MainWindow_mainView()         # link selfInit using .py qt designer file
        self._ui.setupUi(self, self._model)                      # init self


        # set demo mode
        #self.demoMode()

        # connect widgets to controller
        #self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        #self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        # connect 1st Tier (leftmost) button clicks to controller
        self._ui.ux_pButton_Orders.clicked.connect(lambda: self._main_controller.buttonClick_tier1(1))
        self._ui.ux_pButton_Clients.clicked.connect(lambda: self._main_controller.buttonClick_tier1(2))
        self._ui.ux_pButton_Products.clicked.connect(lambda: self._main_controller.buttonClick_tier1(3))
        self._ui.ux_pButton_Invoicing.clicked.connect(lambda: self._main_controller.buttonClick_tier1(4))
        self._ui.ux_pButton_Statistics.clicked.connect(lambda: self._main_controller.buttonClick_tier1(5))
        self._ui.ux_pButton_Settings.clicked.connect(lambda: self._main_controller.buttonClick_tier1(6))

        # connect button click that changes mainView in MainWindow
        self._ui.ux_pButton_newOrder.clicked.connect(lambda: self._main_controller.change_mainView(1))
        self._ui.ux_pButton_addClient.clicked.connect(lambda: self._main_controller.change_mainView(3))
        self._ui.ux_pButton_searchEditClients.clicked.connect(lambda: self._main_controller.change_mainView(4))
        self._ui.ux_pButton_addProduct.clicked.connect(lambda: self._main_controller.change_mainView(5))
        self._ui.ux_pButton_newInvoice.clicked.connect(lambda: self._main_controller.change_mainView(7))
        self._ui.ux_pButton_sendInvoice.clicked.connect(lambda: self._main_controller.change_mainView(8))

        ################################
        #  newOrder Page connections
        ################################
        self._ui.ux_pButton_addProdToOrd.clicked.connect(lambda: self._main_controller.addProd_toNewOrder(
                                                                            self._ui.ux_tableWidget_curProducts.currentRow()))
        self._ui.ux_pButton_compOrder.clicked.connect(lambda: self._main_controller.removeProd_fromNewOrder(self._ui.ux_tableWidget_orderProducts.currentRow()))
        self._ui.ux_pButton_revAndComp.clicked.connect(lambda: self._main_controller.newOrder_reviewOrder(self._ui.ux_lineEdit_orderNumber.text(),
                                                                                                          self._ui.ux_comboBox_clientName.currentIndex(),
                                                                                                          self._ui.ux_lineEdit_deliveryDate.text()))

        self._ui.ux_tableWidget_orderProducts.itemDoubleClicked.connect(lambda: self._main_controller.currentItemChanged(self._ui.ux_tableWidget_orderProducts.selectedIndexes()))
        self._ui.ux_tableWidget_orderProducts.cellChanged.connect(lambda: self._main_controller.productAmountChangedInList(self._ui.ux_tableWidget_orderProducts.item(self._model.prodsInOrdrList_selectedIndices[0],
                                                                                                                                           self._model.prodsInOrdrList_selectedIndices[1])))
           # self._main_controller.productAmountChangedInList(self._ui.ux_tableWidget_orderProducts.item(self._model.prodsInOrdrList_selectedIndices[0], self._model.prodsInOrdrList_selectedIndices[0]))
        #)    #itemChanged.connect(lambda: self._main_controller.currentItemChanged())

        ################################
        #  addClient Page connections
        ################################
        self._ui.ux_pButton_addClient.clicked.connect(lambda: self._main_controller.cntrl_addNewClient(
                                                                         self._ui.ux_lineEdit_newClientName.text(),
                                                                         self._ui.ux_lineEdit_addressLine1.text(),
                                                                         self._ui.ux_lineEdit_addressLine2.text(),
                                                                         self._ui.ux_lineEdit_newClientPhone.text(),
                                                                         self._ui.ux_lineEdit_newClientEmail.text()))

        ######################################
        #  searchEditClients Page connections
        ######################################
        self._ui.ux_pButton_searchEditClients_editClientInfo.clicked.connect(
            self._main_controller.searchEditClients_enableEditInfo_buttonClick)
        self._ui.ui_ListView_searchEditClients_nameSearchList.doubleClicked[QtCore.QModelIndex].connect(
            self.on_searchEditClients_listViewDoubleClick)
        self._ui.ux_pButton_searchEditClients_finalizeInfo.clicked.connect(lambda:
                                                   self._main_controller.searchEditClients_finalizeInfo_buttonClick(
                                                       self._ui.ux_lineEdit_searchEditClients_cNameOut.text(),
                                                       self._ui.ux_lineEdit_searchEditClients_address1Out.text(),
                                                       self._ui.ux_lineEdit_searchEditClients_address2Out.text(),
                                                       self._ui.ux_lineEdit_searchEditClients_cPhoneOut.text(),
                                                       self._ui.ux_lineEdit_searchEditClients_cEmailOut.text()))
        self._ui.ux_lineEdit_searchEditClients_clientNameSearch.textChanged.connect(lambda:
                                                self._main_controller.searchClientNames_byName(
                                                    self._ui.ux_lineEdit_searchEditClients_clientNameSearch.text()))

        ######################################
        #  addProduct Page connections
        ######################################
        self._ui.ux_pButton_newProduct_addProd.clicked.connect(lambda:
                                                    self._main_controller.newProduct_addProduct_buttonClick(
                                                        self._ui.ux_lineEdit_newProduct_name.text(),
                                                        self._ui.ux_textEdit_newProduct_description.toPlainText(),
                                                        self._ui.ux_lineEdit_newProduct_price.text()))

        ######################################
        #  New Invoice Page connections
        ######################################
        self._ui.ux_lineEdit_newInvoice_clientNameSearch.textChanged.connect(lambda:
                                                                             self._main_controller.searchClientNames_byName(
                                                                                 self._ui.ux_lineEdit_newInvoice_clientNameSearch.text()))

        ######################################
        #  New Invoice Create and Send Page connections
        ######################################
        self._ui.ui_ListView_newInvoiceCandS_orderSearchList.doubleClicked[QtCore.QModelIndex].connect(
            self._main_controller.on_newInvoiceCandS_orderSearchListDoubleClick)
        self._ui.ux_lineEdit_newInvoiceCandS_taxApplied.textChanged.connect(lambda: self._main_controller.on_newInvoiceCandS_taxValueChanged(
                                                                                self._ui.ux_lineEdit_newInvoiceCandS_taxApplied.text(),
                                                                                self._ui.ux_lineEdit_newInvoiceCandS_orderSubTotal.text()))
        self._ui.ux_pButton_newInvoiceCandS_createAndSendInvoice.clicked.connect(lambda: self._main_controller.send_invoiceData_toBrowser(
            self._ui.ux_lineEdit_newInvoiceCandS_orderNumber.text(),
            self._ui.ux_lineEdit_newInvoiceCandS_orderSubTotal.text(),
            self._ui.ux_lineEdit_newInvoiceCandS_taxApplied.text(),
            self._ui.ux_lineEdit_newInvoiceCandS_orderTotal.text()
        ))
        self._ui.ux_pButton_newInvoiceCandS_showAllOrders.clicked.connect(self._main_controller.on_newInvoiceCandS_showAllOrders_clicked)
        self._ui.ux_pButton_newInvoiceCandS_ShowUnsentOrders.clicked.connect(self._main_controller.on_newInvoiceCandS_showAllUnsentOrders_clicked)

        # hide widgets which are invisible on start (e.g. newOrders pButton)
        #self.hide_secondLvlMenu_widgets()

        # listen for model event signals
        #self._model.amount_changed.connect(self.on_amount_changed)
        self._model.mainView_changed.connect(self.on_mainView_changed)
        self._model.currentTier2Buttons_changed.connect(self.on_tier1_buttonClick)
        self._model.show_message_box.connect(self.on_show_message_box)
        self._model.call_success.connect(self.on_call_returnValue_received)
        self._model.searchEditClients_searchClientNames_newValues.connect(self.on_searchEditClients_newValues)
        self._model.searchEditClients_clientInfoDoubleClick.connect(self.on_searchEditClients_clientInfoDoubleClick)
        self._model.searchEditClients_editModeChanged.connect(self.on_searchEditClients_editModeChanged)
        self._model.updatedClientList_NameId.connect(self.on_updatedClientList_NameId)
        self._model.updated_ProdNotInOrderList.connect(self.on_updatedProdNotInOrderList)
        self._model.updated_ProdInOrderList.connect(self.on_updatedProdInOrderList)

        # newOrder model event signals
        self._model.addNewOrderSuccess_newOrderNum.connect(self.on_newOrderSuccess_getNextOrderNum)

        # newInvoice model event signals
        self._model.updated_newInvoice_clientList.connect(self.on_newInvoice_newClientList)
        self._model.updated_orderList.connect(self.on_newInvoiceCandS_newOrderList)
        self._model.updated_orderTotal.connect(self.on_newInvoiceCandS_updatedTaxValue)

        self._model.updated_orderData.connect(self.on_newInvoiceCandS_showOrderData)

        self.hide_secondLvlMenu_widgets()

        # set a default value
        #self._main_controller.change_amount(42)

    def demoMode(self):
        self._ui.ux_pButton_searchEditOrders.setDisabled(True)
        self._ui.ux_pButton_searchEditProducts.setDisabled(True)
        self._ui.ux_pButton_newInvoice.setDisabled(True)
        self._ui.ux_pButton_searchEditInvoices.setDisabled(True)
        self._ui.ux_pButton_summaryView.setDisabled(True)
        self._ui.ux_pButton_searchView.setDisabled(True)
        self._ui.ux_pButton_settings.setDisabled(True)

    ####################################################################################################################
    #   MainWindow functions called when model updates
    ####################################################################################################################

    def Set_Tier2Buttons_noArrows(self):
        self._ui.ux_pButton_newOrder.setText("New Order")
        self._ui.ux_pButton_searchEditOrders.setText("Search/Edit Orders")
        self._ui.ux_pButton_newClient.setText("Add New Client")
        self._ui.ux_pButton_editClient.setText("Search/Edit Client Info.")
        self._ui.ux_pButton_addProduct.setText("Add New Product")
        self._ui.ux_pButton_editProduct.setText("Search/Edit Product Info.")
        self._ui.ux_pButton_newInvoice.setText("Create New Invoice")
        self._ui.ux_pButton_sendInvoice.setText("Create and Send Invoice")
        self._ui.ux_pButton_searchInvoice.setText("Search Invoices")
        self._ui.ux_pButton_summaryView.setText("Summary View")
        self._ui.ux_pButton_searchView.setText("Search and View")


    # pyqtSlot and function to change the main window layout according to tier1 (leftmost) button clicks
    @pyqtSlot(int)
    def on_mainView_changed(self, value):
        #self.Set_Tier2Buttons_noArrows()
        if value == 0: self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_welcomeLayout)
        elif value == 1:    # set newOrders page and init fields with relevant data
            self._ui.ux_pButton_newOrder.setText("New Order \u27a4")
            self._ui.ux_pButton_orders.setText("Orders \u27a4")
            self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_newOrderLayout)
            self._ui.ux_lineEdit_orderNumber.setText(self._model.getNextOrderNum())
            self._ui.ux_lineEdit_deliveryDate.setText(self._model.currentDate)
            # self._ui.ux_comboBox_clientName.clear()
            # for (x, y) in self._model.currentClientList:
            #     self._ui.ux_comboBox_clientName.addItem(x)
            # self._ui.ux_lineEdit_deliveryDate.setText(self._model.currentDate)
            # for (x, y) in self._model.getAllProducts():
            #     self._ui.ux_tableWidget_curProducts.set

        elif value == 3:
            self._ui.ux_pButton_clients.setText("Clients \u27a4")
            self._ui.ux_pButton_newClient.setText("Add New Client \u27a4")
            self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_newClientLayout)
        elif value == 4:
            self._ui.ux_pButton_clients.setText("Clients \u27a4")
            self._ui.ux_pButton_editClient.setText("Search/Edit Client Info. \u27a4")
            clients = self._model.getAllClients()
            self._ui.model_listView_searchEditClients_nameSearchList.clear()
            self._ui.model_listView_searchEditClients_NameIdList.clear()
            self._ui.model_listView_searchEditClients_NameIdList = clients
            for (x,y) in clients:
                item = QStandardItem(x)
                item.setData(y)
                self._ui.model_listView_searchEditClients_nameSearchList.appendRow(item)
            self._ui.ux_pButton_searchEditClients_finalizeInfo.setDisabled(True)
            self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_searchEditClientsLayout)
        elif value == 5:
            self._ui.ux_pButton_products.setText("Products \u27a4")
            self._ui.ux_pButton_addProduct.setText("Add New Product \u27a4")
            self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_newProductLayout)
        elif value == 7:
            self._ui.ux_pButton_invoicing.setText("Invoicing \u27a4")
            self._ui.ux_pButton_newInvoice.setText("Create New Invoice \u27a4")
            clients = self._model.getAllClients()
            self._ui.model_listView_newInvoice_nameSearchList.clear()
            self._ui.model_listView_newInvoice_NameIdList.clear()
            self._ui.model_listView_newInvoice_NameIdList = clients
            for (x, y) in clients:
                item = QStandardItem(x)
                item.setData(y)
                self._ui.model_listView_newInvoice_nameSearchList.appendRow(item)
            self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_newInvoiceLayout)
        elif value == 8:
            self._ui.ux_pButton_invoicing.setText("Invoicing \u27a4")
            self._ui.ux_pButton_sendInvoice.setText("Create and Send Invoice \u27a4")
            self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_newInvoiceCandSLayout)

    # signal received after each db call
    @pyqtSlot(int)
    def on_call_returnValue_received(self, value):
        current_view = self._model.currentView
        if current_view == 3:  # if currently in Add New Client view
            if value == 1:  # if adding a new client was successful
                self._ui.ux_lineEdit_newClientEmail.clear()
                self._ui.ux_lineEdit_newClientPhone.clear()
                self._ui.ux_lineEdit_newClientName.clear()
                self._ui.ux_lineEdit_addressLine1.clear()
                self._ui.ux_lineEdit_addressLine2.clear()
            else:
                # nothing => client was not successfully added, thus info stays put
                return
        else:
            # nothing
            return

    @pyqtSlot(tuple)
    def on_show_message_box(self, value):
        (title, text) = value
        QMessageBox.about(self, title, text)

    @pyqtSlot(list)
    def on_updatedClientList_NameId(self, nameList):
        if self._model.currentView == 1:   # if current view is newOrder page
            self._ui.ux_comboBox_clientName.clear()
            #print(nameList)
            for (x, y) in nameList:
                self._ui.ux_comboBox_clientName.addItem(x)
        return

    ####################################################################################################################
    #   MainWindow pButton functions/pyqtSlots
    ####################################################################################################################

    # def Set_Tier1Buttons_noArrows(self):
    #     self._ui.ux_pButton_Orders.setText("Orders")
    #     self._ui.ux_pButton_Clients.setText("Clients")
    #     self._ui.ux_pButton_Products.setText("Products")
    #     self._ui.ux_pButton_Invoicing.setText("Invoicing")
    #     self._ui.ux_pButton_statistics.setText("Statistics")
    #     self._ui.ux_pButton_settings.setText("Settings")

    # signal received from model after one of the leftmost buttons is clicked
    @pyqtSlot(int)
    def on_tier1_buttonClick(self, value):
        if value == 1:
            if (self._ui.ux_pButton_newOrder.isHidden()):
                self._ui.ux_pButton_newOrder.setHidden(0)
                self._ui.ux_pButton_searchEditOrders.setHidden(0)
            else:
                self._ui.ux_pButton_newOrder.setHidden(1)
                self._ui.ux_pButton_searchEditOrders.setHidden(1)
        elif value == 2:
            if self._ui.ux_pButton_addClient.isHidden():
                self._ui.ux_pButton_addClient.setHidden(0)
                self._ui.ux_pButton_searchEditClients.setHidden(0)
            else:
                self._ui.ux_pButton_addClient.setHidden(1)
                self._ui.ux_pButton_searchEditClients.setHidden(1)


    def hide_secondLvlMenu_widgets(self):
        self._ui.ux_pButton_newOrder.setHidden(1)
        self._ui.ux_pButton_searchEditOrders.setHidden(1)
        self._ui.ux_pButton_addProduct.setHidden(1)
        self._ui.ux_pButton_searchEditProducts.setHidden(1)
        self._ui.ux_pButton_addClient.setHidden(1)
        self._ui.ux_pButton_searchEditClients.setHidden(1)
        self._ui.ux_pButton_newInvoice.setHidden(1)
        self._ui.ux_pButton_searchEditInvoices.setHidden(1)
        self._ui.ux_pButton_sendInvoice.setHidden(1)
        self._ui.ux_pButton_searchAndView.setHidden(1)
        self._ui.ux_pButton_summaryView.setHidden(1)
        self._ui.ux_pButton_sendMultInvoices.setHidden(1)



    ####################################################################################################################
    #   newOrders page functions and pyqtslots
    ####################################################################################################################

    @pyqtSlot(list)
    def on_updatedProdNotInOrderList(self, values):
        row = 0
        self._ui.ux_tableWidget_curProducts.setRowCount(len(values))
        #print(values)
        for (id, name, description, price, date) in values:
            self._ui.ux_tableWidget_curProducts.setItem(row, 0, QTableWidgetItem(name))
            priceLen = len(str(price))
            fPrice = str(price)[:(priceLen - 2)] + "," + str(price)[(priceLen-2):]
            self._ui.ux_tableWidget_curProducts.setItem(row, 1, QTableWidgetItem(fPrice))
            row += 1

    @pyqtSlot(list)
    def on_updatedProdInOrderList(self, values):
        row = 0
        self._ui.ux_tableWidget_orderProducts.setRowCount(len(values))
        for listItem in values:
            (pId, name, description, price, date) = listItem[0]
            num = listItem[1]

            # disable single cells code retrieved from: https://stackoverflow.com/a/7756615
            nameItem = QTableWidgetItem(name)
            nameItem.setFlags(QtCore.Qt.ItemIsEnabled)
            self._ui.ux_tableWidget_orderProducts.setItem(row, 0, nameItem)

            priceLen = len(str(price))
            fPrice = str(price)[:(priceLen - 2)] + "," + str(price)[(priceLen-2):]
            totalPrice = price * num
            totalPriceLen = len(str(totalPrice))
            fTotalPrice = str(totalPrice)[:(totalPriceLen - 2)] + "," + str(totalPrice)[(totalPriceLen-2):]

            priceItem = QTableWidgetItem(fPrice)
            priceItem.setFlags(QtCore.Qt.ItemIsEnabled)
            self._ui.ux_tableWidget_orderProducts.setItem(row, 2, priceItem)
            self._ui.ux_tableWidget_orderProducts.setItem(row, 1, QTableWidgetItem(str(num)))
            totalPriceItem = QTableWidgetItem(fTotalPrice)
            totalPriceItem.setFlags(QtCore.Qt.ItemIsEnabled)
            self._ui.ux_tableWidget_orderProducts.setItem(row, 3, totalPriceItem)
            row += 1

    @pyqtSlot(str)
    def on_newOrderSuccess_getNextOrderNum(self, value):
        self._ui.ux_lineEdit_orderNumber.setText(value)


    ####################################################################################################################
    #   searchEditClients page functions and pyqtslots
    ####################################################################################################################

    @pyqtSlot(QtCore.QModelIndex)
    def on_searchEditClients_listViewDoubleClick(self, item):
        (name, id) = self._ui.model_listView_searchEditClients_NameIdList[item.row()]
        self._main_controller.searchEditClients_onClientName_doubleClick(id)

    @pyqtSlot(str, str, str, str, str)
    def on_searchEditClients_clientInfoDoubleClick(self, name, address1, address2, phone, email):
        self._ui.ux_lineEdit_searchEditClients_cNameOut.setText(name)
        self._ui.ux_lineEdit_searchEditClients_address1Out.setText(address1)
        self._ui.ux_lineEdit_searchEditClients_address2Out.setText(address2)
        self._ui.ux_lineEdit_searchEditClients_cPhoneOut.setText(phone)
        self._ui.ux_lineEdit_searchEditClients_cEmailOut.setText(email)
        self._ui.ux_lineEdit_searchEditClients_cNameOut.setReadOnly(True)
        self._ui.ux_lineEdit_searchEditClients_address1Out.setReadOnly(True)
        self._ui.ux_lineEdit_searchEditClients_address2Out.setReadOnly(True)
        self._ui.ux_lineEdit_searchEditClients_cPhoneOut.setReadOnly(True)
        self._ui.ux_lineEdit_searchEditClients_cEmailOut.setReadOnly(True)
        self._ui.ux_pButton_searchEditClients_finalizeInfo.setDisabled(True)

    @pyqtSlot(int)
    def on_searchEditClients_editModeChanged(self, value):
        if value == 1:
            # change values in lineEdit boxes to be modifiable
            self._ui.ux_lineEdit_searchEditClients_cNameOut.setReadOnly(False)
            self._ui.ux_lineEdit_searchEditClients_address1Out.setReadOnly(False)
            self._ui.ux_lineEdit_searchEditClients_address2Out.setReadOnly(False)
            self._ui.ux_lineEdit_searchEditClients_cPhoneOut.setReadOnly(False)
            self._ui.ux_lineEdit_searchEditClients_cEmailOut.setReadOnly(False)
            self._ui.ux_pButton_searchEditClients_finalizeInfo.setDisabled(False)
            self._ui.ux_pButton_searchEditClients_editClientInfo.setText("Cancel Editing Client Info")
            return
        else:
            self._ui.ux_lineEdit_searchEditClients_cNameOut.setReadOnly(True)
            self._ui.ux_lineEdit_searchEditClients_address1Out.setReadOnly(True)
            self._ui.ux_lineEdit_searchEditClients_address2Out.setReadOnly(True)
            self._ui.ux_lineEdit_searchEditClients_cPhoneOut.setReadOnly(True)
            self._ui.ux_lineEdit_searchEditClients_cEmailOut.setReadOnly(True)
            self._ui.ux_pButton_searchEditClients_finalizeInfo.setDisabled(True)
            self._ui.ux_pButton_searchEditClients_editClientInfo.setText("Edit Client Information")
            return

    @pyqtSlot(list)
    def on_searchEditClients_newValues(self, nameList):
        self._ui.model_listView_searchEditClients_nameSearchList.clear()
        self._ui.model_listView_searchEditClients_NameIdList.clear()
        #print(nameList)
        for (x, y) in nameList:
            item = QStandardItem(x)
            item.setData(y)
            self._ui.model_listView_searchEditClients_nameSearchList.appendRow(item)
        self._ui.model_listView_searchEditClients_NameIdList = nameList

    ####################################################################################################################
    #   newInvoice page functions and pyqtslots
    ####################################################################################################################

    @pyqtSlot(list)
    def on_newInvoice_newClientList(self, nameList):
        self._ui.model_listView_newInvoice_nameSearchList.clear()
        self._ui.model_listView_newInvoice_NameIdList.clear()
        #print(nameList)
        for (x, y) in nameList:
            item = QStandardItem(x)
            item.setData(y)
            self._ui.model_listView_newInvoice_nameSearchList.appendRow(item)
        self._ui.model_listView_newInvoice_NameIdList = nameList

    ####################################################################################################################
    #   newInvoiceCandS page functions and pyqtslots
    ####################################################################################################################
    @pyqtSlot(QStandardItemModel)
    def on_newInvoiceCandS_newOrderList(self, orderList):
        #self._ui.model_listView_searchEditClients_NameIdList.clear()
        #print("DEBUG_fromGUI: " + str(orderList))
        self._ui.ui_ListView_newInvoiceCandS_orderSearchList.show()

    @pyqtSlot(str, str, str, str, str, str, int)
    def on_newInvoiceCandS_showOrderData(self, name, ad1, ad2, ph, em, orderNum, orderSubTotal):
        # set order and client information using new data
        self._ui.ux_lineEdit_newInvoiceCandS_cNameOut.setText(name)
        self._ui.ux_lineEdit_newInvoiceCandS_address1Out.setText(ad1)
        self._ui.ux_lineEdit_newInvoiceCandS_address2Out.setText(ad2)
        self._ui.ux_lineEdit_newInvoiceCandS_cPhoneOut.setText(ph)
        self._ui.ux_lineEdit_newInvoiceCandS_cEmailOut.setText(em)
        self._ui.ux_lineEdit_newInvoiceCandS_orderNumber.setText(orderNum)

        # show order items from updated model values
        self._ui.ui_listView_newInvoiceCandS_orderItems.show()

        # calc and format orderSubTotal
        orderSubTotalLen = len(str(orderSubTotal))
        fOrderSubTotal = str(orderSubTotal)[:(orderSubTotalLen - 2)] + "." + str(orderSubTotal)[(orderSubTotalLen - 2):]
        self._ui.ux_lineEdit_newInvoiceCandS_orderSubTotal.setText(fOrderSubTotal)

        # place default tax percentage
        self._ui.ux_lineEdit_newInvoiceCandS_taxApplied.setText("0")
        self._ui.ux_lineEdit_newInvoiceCandS_taxApplied.setText("5.5")

    @pyqtSlot(str)
    def on_newInvoiceCandS_updatedTaxValue(self, orderTotal):
        self._ui.ux_lineEdit_newInvoiceCandS_orderTotal.setText(orderTotal)

