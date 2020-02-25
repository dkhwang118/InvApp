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
from PyQt5.QtCore import pyqtSlot, Qt
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



        # set the ListView as an update connection
        self._model.updated_ClientId_All.connect(self.viewUpdate_ClientList_AllClients)

        ##################################################################
        #   1. Window Opens and Displays all Names in DB to search from
        ##################################################################
        # 1.1 Get all clients from DB and show in ui_ListView_searchNamesPopup_nameSearchList



        ##################################################################
        #   2a. User Double-Clicks a name in box
        ##################################################################

        ##################################################################
        #   2b. User inputs text into search box
        ##################################################################

        ##################################################################
        #
        ##################################################################


    @pyqtSlot(list)
    def viewUpdate_ClientList_AllClients(self, nameList):
        self._ui.ui_ListView_searchNamesPopup_nameSearchList.
        print(nameList)
        for (x, y) in nameList:
            self._ui.ui_ListView_searchNamesPopup_nameSearchList.
        return
        ##################################################################
        #
        ##################################################################


