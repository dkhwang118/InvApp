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
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model  # connect App to MainView
        self._main_controller = main_controller  # connect cntrl
        self._ui = UI_SearchSelect_ClientbyName()  # link selfInit using .py qt designer file
        self._ui.setupUi(self, self._model, self._main_controller)  # init self

        self.setWindowModality(Qt.ApplicationModal)


