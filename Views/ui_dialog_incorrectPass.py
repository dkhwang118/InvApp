# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_incorrectPass.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_incorrectPass(object):
    def setupUi(self, ui_dialog_incorrectPass):
        ui_dialog_incorrectPass.setObjectName("ui_dialog_incorrectPass")
        ui_dialog_incorrectPass.resize(400, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_dialog_incorrectPass.sizePolicy().hasHeightForWidth())
        ui_dialog_incorrectPass.setSizePolicy(sizePolicy)
        ui_dialog_incorrectPass.setFixedSize(ui_dialog_incorrectPass.size())


        self.ux_pButton_incorrectPassConfirm = QtWidgets.QPushButton(ui_dialog_incorrectPass)
        self.ux_pButton_incorrectPassConfirm.setGeometry(QtCore.QRect(290, 130, 101, 31))
        self.ux_pButton_incorrectPassConfirm.setObjectName("ux_pButton_incorrectPassConfirm")
        self.ui_incorrectPass = QtWidgets.QLabel(ui_dialog_incorrectPass)
        self.ui_incorrectPass.setGeometry(QtCore.QRect(6, 3, 391, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui_incorrectPass.setFont(font)
        self.ui_incorrectPass.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_incorrectPass.setWordWrap(True)
        self.ui_incorrectPass.setObjectName("ui_incorrectPass")
        ui_dialog_incorrectPass.setSizePolicy(sizePolicy)

        self.retranslateUi(ui_dialog_incorrectPass)
        QtCore.QMetaObject.connectSlotsByName(ui_dialog_incorrectPass)

    def retranslateUi(self, ui_dialog_incorrectPass):
        _translate = QtCore.QCoreApplication.translate
        ui_dialog_incorrectPass.setWindowTitle(_translate("ui_dialog_incorrectPass", "Dialog"))
        self.ux_pButton_incorrectPassConfirm.setText(_translate("ui_dialog_incorrectPass", "OK"))
        self.ui_incorrectPass.setText(_translate("ui_dialog_incorrectPass", "Incorrect Password Input. Please Try Again."))
