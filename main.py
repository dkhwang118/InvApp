# main.py
# 101819 - DKH

import sqlite3 as sqlite
from PyQt5.QtWidgets import QApplication, QLabel





############################################
#   Qt Initialization
############################################

args = [] # command-line args to application

# init Qt App w/ args
app = QApplication(args)

# set Qt app style to 'Fusion'
app.setStyle('Fusion')


###################################################################
#   Define Qt Widgets
###################################################################





##############################################
#   Qt Runtime
##############################################

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