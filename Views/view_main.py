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


from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Views.view_main_layout import Ui_MainWindow_mainView


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model                         # connect App to MainView
        self._main_controller = main_controller     # connect cntrl
        self._ui = Ui_MainWindow_mainView()         # link selfInit using .py qt designer file
        self._ui.setupUi(self)                      # init self


        # connect widgets to controller
        #self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        #self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        # connect 1st Tier (leftmost) button clicks to controller
        self._ui.ux_pButton_orders.clicked.connect(lambda: self._main_controller.buttonClick_tier1(1))
        self._ui.ux_pButton_clients.clicked.connect(lambda: self._main_controller.buttonClick_tier1(2))
        self._ui.ux_pButton_products.clicked.connect(lambda: self._main_controller.buttonClick_tier1(3))
        self._ui.ux_pButton_invoicing.clicked.connect(lambda: self._main_controller.buttonClick_tier1(4))
        self._ui.ux_pButton_statistics.clicked.connect(lambda: self._main_controller.buttonClick_tier1(5))
        self._ui.ux_pButton_settings.clicked.connect(lambda: self._main_controller.buttonClick_tier1(6))

        # connect button click that changes mainView in MainWindow
        self._ui.ux_pButton_newOrder.clicked.connect(lambda: self._main_controller.change_mainView(1))
        self._ui.ux_pButton_newClient.clicked.connect(lambda: self._main_controller.change_mainView(3))
        self._ui.ux_pButton_editClient.clicked.connect(lambda: self._main_controller.change_mainView(4))

        # connect buttons that query/change db information
        self._ui.ux_pButton_addClient.clicked.connect(lambda: self._main_controller.cntrl_addNewClient(self._ui.ux_lineEdit_newClientName.text(),
                                                                                                 self._ui.ux_lineEdit_addressLine1.text(),
                                                                                                 self._ui.ux_lineEdit_addressLine2.text(),
                                                                                                 self._ui.ux_lineEdit_newClientPhone.text(),
                                                                                                 self._ui.ux_lineEdit_newClientEmail.text()))

        # hide widgets which are invisible on start (e.g. newOrders pButton)
        self.hide_secondLvlMenu_widgets()

        # listen for model event signals
        #self._model.amount_changed.connect(self.on_amount_changed)
        self._model.mainView_changed.connect(self.on_mainView_changed)
        self._model.currentTier2Buttons_changed.connect(self.on_tier1_buttonClick)
        self._model.show_message_box.connect(self.on_show_message_box)
        self._model.call_success.connect(self.on_call_returnValue_received)

        # set a default value
        #self._main_controller.change_amount(42)

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
                # nothing
                return
        else:
            # nothing
            return

    # signal received from model after one of the leftmost buttons is clicked
    @pyqtSlot(int)
    def on_tier1_buttonClick(self, value):
        if value == 0:
            self.hide_secondLvlMenu_widgets()
        elif value == 1:    # Orders button clicked
            self.hide_secondLvlMenu_widgets()
            self._ui.ux_pButton_newOrder.show()
            self._ui.ux_pButton_searchEditOrders.show()
        elif value == 2:
            self.hide_secondLvlMenu_widgets()
            self._ui.ux_pButton_newClient.show()
            self._ui.ux_pButton_editClient.show()
        elif value == 3:
            self.hide_secondLvlMenu_widgets()
            self._ui.ux_pButton_addProduct.show()
            self._ui.ux_pButton_editProduct.show()
        elif value == 4:
            self.hide_secondLvlMenu_widgets()
            self._ui.ux_pButton_newInvoice.show()
            self._ui.ux_pButton_searchInvoice.show()
            self._ui.ux_pButton_sendInvoice.show()
        elif value == 5:
            self.hide_secondLvlMenu_widgets()
            self._ui.ux_pButton_searchView.show()
            self._ui.ux_pButton_summaryView.show()
        elif value == 6:
            self.hide_secondLvlMenu_widgets()

    # pyqtSlot and function to change the main window layout according to tier1 (leftmost) button clicks
    @pyqtSlot(int)
    def on_mainView_changed(self, value):
        if value == 0: self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_welcomeLayout)
        elif value == 1: self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_newOrderLayout)
        elif value == 3: self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_newClientLayout)
        elif value == 4:
            clients = self._model.getAllClients()
            self._ui.model_listView_searchEditClients_nameSearchList.clear()
            #print(clients)
            for (x,) in clients:
                self._ui.model_listView_searchEditClients_nameSearchList.appendRow(QStandardItem(x))
            self._ui.stackedLayoutWidget.setCurrentWidget(self._ui.widget_searchEditClientsLayout)

    @pyqtSlot(tuple)
    def on_show_message_box(self, value):
        (title, text) = value
        QMessageBox.about(self, title, text)

    # @pyqtSlot(int)
    # def on_amount_changed(self, value):
    #     self._ui.spinBox_amount.setValue(value)
    #
    # @pyqtSlot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)
    #
    # @pyqtSlot(bool)
    # def on_enable_reset_changed(self, value):
    #     self._ui.pushButton_reset.setEnabled(value)

    def hide_secondLvlMenu_widgets(self):
        self._ui.ux_pButton_newOrder.setHidden(1)
        self._ui.ux_pButton_searchEditOrders.setHidden(1)
        self._ui.ux_pButton_addProduct.setHidden(1)
        self._ui.ux_pButton_editProduct.setHidden(1)
        self._ui.ux_pButton_newClient.setHidden(1)
        self._ui.ux_pButton_editClient.setHidden(1)
        self._ui.ux_pButton_newInvoice.setHidden(1)
        self._ui.ux_pButton_searchInvoice.setHidden(1)
        self._ui.ux_pButton_sendInvoice.setHidden(1)
        self._ui.ux_pButton_searchView.setHidden(1)
        self._ui.ux_pButton_summaryView.setHidden(1)


