# main.py
# 101819 - DKH

import sqlite3 as sqlite
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt






############################################
#   Qt Initialization
############################################

# command-line args to application
args = []

# init Qt App w/ args
app = QtWidgets.QApplication(args)

# set Qt app style to 'Fusion'
app.setStyle('Fusion')


###################################################################
#   Define Qt Widgets
###################################################################

UxWelcomeLabel = QtWidgets.QLabel('Welcome')


# UiMainWindow - Main GUI Window for application
class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # init itself
        QtWidgets.QMainWindow.__init__(self)

        # declare starting "Central Widget" => starting widget should be QLabel "Welcome"
        self.setCentralWidget(UxWelcomeLabel)


##############################################
#   Qt Runtime
##############################################


mainWindow = UiMainWindow()
mainWindow.show()
app.exec_()









########################################
#   sqlite3 db code to start a db
########################################
# conn = sqlite.connect('test.db')
# c = conn.cursor()
# c.execute("PRAGMA key='password'")
# c.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
# c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
# conn.commit()
# c.close()