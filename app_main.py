###########################################################################
#
#   app_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   Edited by: David K. Hwang
#
#
############################################################################

import sys
from PyQt5.QtWidgets import QApplication
from Model.model_main import Model
from Controller.controller_main import MainController
from Views.view_main_ui import Ui_MainWindow_mainView
from pathlib import Path
from Views.view_main import MainView
from Crypto.PublicKey import RSA

############################################
#   Qt Initialization
############################################

# command-line args to application
#args = []

# init Qt App w/ args
#app = QApplication(args)

# set Qt app style to 'Fusion'
#app.setStyle('Fusion')


# main application class that connects the MVC framework
class AppMain(QApplication):
    def __init__(self, sys_argv):
        super(AppMain, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_controller.define_view(self.main_view)
        self.main_view.show()


if __name__ == '__main__':
    appRun = AppMain(sys.argv)
    sys.exit(appRun.exec_())
