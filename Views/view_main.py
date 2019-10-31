###########################################################################
#
#   view_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   Edited by: David K. Hwang
#
#
#   pyuic5 main_view.ui -o ..\views\main_view_ui.py to convert .ui to .py
#
############################################################################


from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from Views.view_main_ui import Ui_MainWindow_mainView


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model #connect App to MainView
        self._main_controller = main_controller # connect cntrl
        self._ui = Ui_MainWindow_mainView() # link selfInit using .py qt designer file
        self._ui.setupUi(self) # init self

        # connect widgets to controller
        self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))
        self._ui.ux_pButton_orders.clicked.connect()

        # listen for model event signals
        #self._model.amount_changed.connect(self.on_amount_changed)
        #self._model.even_odd_changed.connect(self.on_even_odd_changed)
        #self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        #self._main_controller.change_amount(42)

    # @pyqtSlot(int)
    # def on_amount_changed(self, value):
    #     self._ui.spinBox_amount.setValue(value)
    #
    # @pyqtSlot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)
    #
    # @pyqtSlot(bool)
    # def on_enable_reset_changed(self, value):
    #     self._ui.pushButton_reset.setEnabled(value)