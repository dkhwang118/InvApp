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
from pathlib import Path
from Views.view_main import MainView
from Views.view_startup import StartupView
from Model.model_sql_db_utils import *
from Views.view_incorrectPassDialog import IncorrectPassDialog
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets, QtCore
from Views.view_SearchSelect_ClientByName import view_SearchSelect_ClientByName

############################################
#   Qt Initialization
############################################

# idea from: https://leomoon.com/journal/python/high-dpi-scaling-in-pyqt5/
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)    #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)       #use highdpi icons

# command-line args to application
args = []

# init Qt App w/ args
app = QApplication(args)

appFont = app.font()
appFont.setPixelSize(14)
app.setFont(appFont)

# set Qt app style to 'Fusion'
app.setStyle('Fusion')

# main application class that connects the MVC framework
class AppMain(QApplication):
    def __init__(self, sys_argv):

        # init main
        super(AppMain, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.startup_view = StartupView(self.model, self.main_controller)
        self.pass_dialog = IncorrectPassDialog(self.main_controller)
        #self.searchSelect_clientByName = view_SearchSelect_ClientByName(self.model, self.main_controller)


        self.main_controller.define_startupView(self.startup_view)
        self.main_controller.define_mainView(self.main_view)
        self.main_controller.define_passDialog(self.pass_dialog)
        #self.main_controller.define_searchClients(self.searchSelect_clientByName)

        # show initial startup ui
        self.startup_view.show()


if __name__ == '__main__':

    appRun = AppMain(sys.argv)
    sys.exit(appRun.exec_())
