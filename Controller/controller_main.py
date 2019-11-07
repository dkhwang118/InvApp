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
    def __init__(self, model):
        super().__init__()

        self._model = model

    def define_view(self, qObj):
        self._mainView = qObj


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