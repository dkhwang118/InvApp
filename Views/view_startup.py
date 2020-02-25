###########################################################################
#
#   view_startup.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   Edited by: David K. Hwang
#
#   pyuic5 Views\view_main_ui.ui -o Views\view_main_ui.py
#   to convert .ui to .py
#
############################################################################

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from Views.view_firstStart_layout import Ui_StartPage


class StartupView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model                         # connect App to MainView
        self._main_controller = main_controller     # connect cntrl
        self._ui = Ui_StartPage()         # link selfInit using .py qt designer file
        self._ui.setupUi(self, model.firstTimeStartup)                      # init self

        # connect widgets to controller
        self._ui.ux_pButton_login.setAutoDefault(True)

        #self._ui.ux_pButton_login.clicked.connect(lambda: self._main_controller.buttonClick_passwordLogin(self._ui.ux_lineEdit_passwordInput.text()))
        self._ui.ux_pButton_login.clicked.connect(self._main_controller.buttonClick_StartPage_Login)

