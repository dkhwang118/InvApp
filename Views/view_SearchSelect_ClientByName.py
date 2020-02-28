######################################################################################################################
#
#   view_SearchSelect_ClientByName
#
#   UI Qt Design Layout for a pop-up page that allows user to search for a client by name and select them
#
######################################################################################################################

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, Qt, QObject
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Views.QtLayouts.view_SearchSelect_ClientByName_Layout import UI_SearchSelect_ClientbyName


class view_SearchSelect_ClientByName(QMainWindow):

    ####################
    #   Global Vars
    ####################
    NameList_Full = []              # Full list of names
    NameList = []                   # Currently listed names
    NameOut = ""                    # Current Name Output
    AddressOut1 = ""
    AddressOut2 = ""
    PhoneOut = ""
    EmailOut = ""

    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model  # connect App to MainView
        self._main_controller = main_controller  # connect cntrl
        self._ui = UI_SearchSelect_ClientbyName()  # link selfInit using .py qt designer file
        self._ui.setupUi(self, self._model, self._main_controller)  # init self

        self.setWindowModality(Qt.ApplicationModal)


        # set the user input text in the LineEdit connection
        self._ui.ux_lineEdit_searchEditClients_clientNameSearch.textChanged.connect(lambda:
                                                                                    self._main_controller.viewSearchSelectClientPopup_searchTextChanged(
                                                                                        self._ui.ux_lineEdit_searchEditClients_clientNameSearch.text()))

        # when the model updates the Client List based on user input, the signal is received and view is updated
        self._model.viewUpdate_searchSelectClientPopup_searchTextChanged.connect(self.viewUpdate_ClientList_searchTextChanged)

        self._ui.ui_ListView_searchNamesPopup_nameSearchList.doubleClicked[QtCore.QModelIndex].connect(
            self._main_controller.viewSearchSelectClientPopup_on_nameDoubleClick)

        self._model.viewUpdate_searchSelectClientPopup_clientInfoChanged.connect(self.on_searchSelectClients_updateClientInfo)
        self._ui.ux_pButton_searchClientsPopup_SelectClient.clicked.connect(self._main_controller.viewSearchSelectClientPopup_on_clientSelected)

        ##################################################################
        #   1. Window Opens and Displays all Names in DB to search from
        ##################################################################
        # 1.1 Get all clients from DB and show in ui_ListView_searchNamesPopup_nameSearchList
        model_nameList = QStandardItemModel()
        for (name, id) in self._main_controller.controller_getAllClientNames():
            item = QStandardItem(name)
            item.setData(id)
            model_nameList.appendRow(item)

        self._ui.ui_ListView_searchNamesPopup_nameSearchList.setModel(model_nameList)
        self._model.List_searchSelectClientPopup_searchList = model_nameList



        ##################################################################
        #   2a. User Double-Clicks a name in box
        ##################################################################

        ##################################################################
        #   2b. User inputs text into search box
        ##################################################################

        ##################################################################
        #
        ##################################################################


    @pyqtSlot(QStandardItemModel)
    def viewUpdate_ClientList_AllClients(self, nameList):
        self._ui.ui_ListView_searchNamesPopup_nameSearchList.setModel(nameList)
        return

    @pyqtSlot(QStandardItemModel)
    def viewUpdate_ClientList_searchTextChanged(self, values):
        self._ui.ui_ListView_searchNamesPopup_nameSearchList.setModel(values)

    @pyqtSlot(tuple)
    def on_searchSelectClients_updateClientInfo(self, tup):
        # get data on item that was double-clicked
        self._ui.ui_label_searchClientsPopup_cNameOut.setText(tup[0])
        self._ui.ui_label_searchClientsPopup_address1Out.setText(tup[1])
        self._ui.ui_label_searchClientsPopup_address2Out.setText(tup[2])
        self._ui.ui_label_searchClientsPopup_cPhoneOut.setText(tup[3])
        self._ui.ui_label_searchClientsPopup_cEmailOut.setText(tup[4])

        ##################################################################
        #
        ##################################################################


