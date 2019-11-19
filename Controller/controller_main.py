###########################################################################
#
#   controller_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   Edited by: David K. Hwang
#
#
############################################################################

from PyQt5.QtCore import QObject, pyqtSlot
from Views.view_main import MainView
from Views.view_startup import StartupView
from Model.model_sql_db_utils import *


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model
        self._self = self

    def define_mainView(self, qObj):
        self._mainView = qObj

    def define_startupView(self, qObj):
        self._startupView = qObj

    @pyqtSlot()
    def buttonClick_order(self):
        self._mainView.on_buttonClick_orders()

    @pyqtSlot(int)
    def change_mainView(self, value):
        self._model.currentView = value

    @pyqtSlot(int)
    def change_amount(self, value):
        self._model.amount = value

        # calculate even or odd
        self._model.even_odd = 'odd' if value % 2 else 'even'

        # calculate button enabled state
        self._model.enable_reset = True if value else False

    @pyqtSlot(str)
    def buttonClick_passwordLogin(self, value):
        # code to tell controller to attempt db connection with given password value
        self._model.db_connection_init(value)

        # after successful connection, show mainview
        main_view = MainView(self._model, self._self)
        main_view.show()
        #self._main_view.show()
