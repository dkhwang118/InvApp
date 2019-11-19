###########################################################################
#
#   model_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   sqlite3 implementation framework by "Adam McQuistan" (https://stackabuse.com/a-sqlite-tutorial-with-python/)
#
#   Edited by: David K. Hwang
#
#
############################################################################

from PyQt5.QtCore import QObject, pyqtSignal
import sqlite3


class Model(QObject):


    # define signals dependent on changes in model
    amount_changed = pyqtSignal(int)
    even_odd_changed = pyqtSignal(str)
    enable_reset_changed = pyqtSignal(bool)

    # define page-change signal
    mainView_changed = pyqtSignal(int)

    @property
    def currentView(self):
        return self._currentView

    @currentView.setter
    def currentView(self, value):
        self._currentView = value
        self.mainView_changed.emit(value)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amount_changed.emit(value)

    @property
    def even_odd(self):
        return self._even_odd

    @even_odd.setter
    def even_odd(self, value):
        self._even_odd = value
        self.even_odd_changed.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._currentView = 0

        self._amount = 0
        self._even_odd = ''
        self._enable_reset = False