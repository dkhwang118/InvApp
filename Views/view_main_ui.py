# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_mainView(object):
    def setupUi(self, MainWindow_mainView):
        MainWindow_mainView.setObjectName("MainWindow_mainView")
        MainWindow_mainView.resize(1200, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_mainView.sizePolicy().hasHeightForWidth())
        MainWindow_mainView.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow_mainView)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 131, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ui_vLayout_viewMain = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ui_vLayout_viewMain.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.ui_vLayout_viewMain.setContentsMargins(0, 0, 0, 0)
        self.ui_vLayout_viewMain.setSpacing(0)
        self.ui_vLayout_viewMain.setObjectName("ui_vLayout_viewMain")
        self.ux_pButton_orders = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_orders.sizePolicy().hasHeightForWidth())
        self.ux_pButton_orders.setSizePolicy(sizePolicy)
        self.ux_pButton_orders.setBaseSize(QtCore.QSize(0, 0))
        self.ux_pButton_orders.setObjectName("ux_pButton_orders")
        self.ui_vLayout_viewMain.addWidget(self.ux_pButton_orders)
        self.ux_pButton_clients = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_clients.sizePolicy().hasHeightForWidth())
        self.ux_pButton_clients.setSizePolicy(sizePolicy)
        self.ux_pButton_clients.setObjectName("ux_pButton_clients")
        self.ui_vLayout_viewMain.addWidget(self.ux_pButton_clients)
        self.ux_pButton_products = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_products.sizePolicy().hasHeightForWidth())
        self.ux_pButton_products.setSizePolicy(sizePolicy)
        self.ux_pButton_products.setObjectName("ux_pButton_products")
        self.ui_vLayout_viewMain.addWidget(self.ux_pButton_products)
        self.ux_pButton_invoicing = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_invoicing.sizePolicy().hasHeightForWidth())
        self.ux_pButton_invoicing.setSizePolicy(sizePolicy)
        self.ux_pButton_invoicing.setObjectName("ux_pButton_invoicing")
        self.ui_vLayout_viewMain.addWidget(self.ux_pButton_invoicing)
        self.ux_pButton_statistics = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_statistics.sizePolicy().hasHeightForWidth())
        self.ux_pButton_statistics.setSizePolicy(sizePolicy)
        self.ux_pButton_statistics.setObjectName("ux_pButton_statistics")
        self.ui_vLayout_viewMain.addWidget(self.ux_pButton_statistics)
        self.ux_pButton_settings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_settings.sizePolicy().hasHeightForWidth())
        self.ux_pButton_settings.setSizePolicy(sizePolicy)
        self.ux_pButton_settings.setObjectName("ux_pButton_settings")
        self.ui_vLayout_viewMain.addWidget(self.ux_pButton_settings)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 270, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow_mainView.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_mainView)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_mainView)

    def retranslateUi(self, MainWindow_mainView):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_mainView.setWindowTitle(_translate("MainWindow_mainView", "MainWindow"))
        self.ux_pButton_orders.setText(_translate("MainWindow_mainView", "Orders"))
        self.ux_pButton_clients.setText(_translate("MainWindow_mainView", "Clients"))
        self.ux_pButton_products.setText(_translate("MainWindow_mainView", "Products"))
        self.ux_pButton_invoicing.setText(_translate("MainWindow_mainView", "Invoicing"))
        self.ux_pButton_statistics.setText(_translate("MainWindow_mainView", "Statistics"))
        self.ux_pButton_settings.setText(_translate("MainWindow_mainView", "Settings"))
        self.label.setText(_translate("MainWindow_mainView", "Welcome!"))
