###########################################################################
#
#   controller_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   Edited by: David K. Hwang
#
#
############################################################################

from PyQt5.QtCore import QObject, pyqtSlot


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
    #   pyqtSlots
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

    @pyqtSlot(str, str, str, str, str)
    def addNewClient(self, name, address1, address2, phone, email):
        self._model.db_addNewClient(name, address1, address2, phone, email)

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
        connected = self._model.db_connection_init(value)

        if connected:
            # after successful connection, show mainview
            self._startupView.hide()
            self._mainView.show()
        else:
            self._incorrectPass.show()


