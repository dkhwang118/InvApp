#####################
#
# test.py
# testfile that opens a .ui file
#
#
#######################



from PyQt5 import QtWidgets, uic
from pathlib import Path

import sys

app = QtWidgets.QApplication([])

win = uic.loadUi(Path("Views/view_main_ui.ui"))  # specify the location of your .ui file

win.show()

sys.exit(app.exec())