########################################################################################################################
#
#   view_incorrectPassDialog.py
#   Created by: David K. Hwang
#
#   view window shown when the incorrect database password has been input upon application startup
#
########################################################################################################################


from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, Qt
from Views.view_incorrectPass_layout import Ui_incorrectPass


class IncorrectPassDialog(QMainWindow):
    def __init__(self, main_controller):
        super().__init__()

        self._main_controller = main_controller     # connect cntrl
        self._ui = Ui_incorrectPass()         # link selfInit using .py qt designer file
        self._ui.setupUi(self)                      # init self
        self.setWindowModality(Qt.ApplicationModal)
        self._ui.ux_pButton_incorrectPassConfirm.setAutoDefault(True)

        # connect push button to controller
        self._ui.ux_pButton_incorrectPassConfirm.clicked.connect(self._main_controller.buttonClick_passDialog)

    @pyqtSlot()
    def on_buttonClick_ok(self):
        self.hide()

