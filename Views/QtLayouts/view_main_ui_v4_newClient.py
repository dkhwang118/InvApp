# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_main_ui_v4_newClient.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_mainView(object):
    def setupUi(self, MainWindow_mainView):
        MainWindow_mainView.setObjectName("MainWindow_mainView")
        MainWindow_mainView.resize(1196, 711)
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
        self.ux_pButton_searchEditOrders = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_searchEditOrders.setGeometry(QtCore.QRect(130, 60, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_searchEditOrders.sizePolicy().hasHeightForWidth())
        self.ux_pButton_searchEditOrders.setSizePolicy(sizePolicy)
        self.ux_pButton_searchEditOrders.setObjectName("ux_pButton_searchEditOrders")
        self.ux_pButton_newOrder = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_newOrder.setGeometry(QtCore.QRect(130, 0, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_newOrder.sizePolicy().hasHeightForWidth())
        self.ux_pButton_newOrder.setSizePolicy(sizePolicy)
        self.ux_pButton_newOrder.setObjectName("ux_pButton_newOrder")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(310, 20, 871, 681))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ui_layout_dynamicMainView = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ui_layout_dynamicMainView.setContentsMargins(0, 0, 0, 0)
        self.ui_layout_dynamicMainView.setObjectName("ui_layout_dynamicMainView")
        self.ui_layout_newOrder = QtWidgets.QGridLayout()
        self.ui_layout_newOrder.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.ui_layout_newOrder.setSpacing(6)
        self.ui_layout_newOrder.setObjectName("ui_layout_newOrder")
        self.ux_lineEdit_newClientName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_lineEdit_newClientName.sizePolicy().hasHeightForWidth())
        self.ux_lineEdit_newClientName.setSizePolicy(sizePolicy)
        self.ux_lineEdit_newClientName.setMinimumSize(QtCore.QSize(200, 0))
        self.ux_lineEdit_newClientName.setObjectName("ux_lineEdit_newClientName")
        self.ui_layout_newOrder.addWidget(self.ux_lineEdit_newClientName, 2, 1, 1, 2)
        self.ux_label_newClientAddress_line2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_newClientAddress_line2.sizePolicy().hasHeightForWidth())
        self.ux_label_newClientAddress_line2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_newClientAddress_line2.setFont(font)
        self.ux_label_newClientAddress_line2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ux_label_newClientAddress_line2.setObjectName("ux_label_newClientAddress_line2")
        self.ui_layout_newOrder.addWidget(self.ux_label_newClientAddress_line2, 6, 0, 1, 1)
        self.ux_lineEdit_addressLine1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_lineEdit_addressLine1.sizePolicy().hasHeightForWidth())
        self.ux_lineEdit_addressLine1.setSizePolicy(sizePolicy)
        self.ux_lineEdit_addressLine1.setMinimumSize(QtCore.QSize(200, 0))
        self.ux_lineEdit_addressLine1.setObjectName("ux_lineEdit_addressLine1")
        self.ui_layout_newOrder.addWidget(self.ux_lineEdit_addressLine1, 5, 1, 1, 2)
        self.ux_pButton_addClient = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ux_pButton_addClient.setMinimumSize(QtCore.QSize(0, 50))
        self.ux_pButton_addClient.setObjectName("ux_pButton_addClient")
        self.ui_layout_newOrder.addWidget(self.ux_pButton_addClient, 13, 3, 1, 1)
        self.ux_lineEdit_addressLine2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_lineEdit_addressLine2.sizePolicy().hasHeightForWidth())
        self.ux_lineEdit_addressLine2.setSizePolicy(sizePolicy)
        self.ux_lineEdit_addressLine2.setMinimumSize(QtCore.QSize(200, 0))
        self.ux_lineEdit_addressLine2.setObjectName("ux_lineEdit_addressLine2")
        self.ui_layout_newOrder.addWidget(self.ux_lineEdit_addressLine2, 6, 1, 1, 2)
        self.ux_label_newClientPhone = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_newClientPhone.sizePolicy().hasHeightForWidth())
        self.ux_label_newClientPhone.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_newClientPhone.setFont(font)
        self.ux_label_newClientPhone.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ux_label_newClientPhone.setObjectName("ux_label_newClientPhone")
        self.ui_layout_newOrder.addWidget(self.ux_label_newClientPhone, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ui_layout_newOrder.addItem(spacerItem, 1, 1, 1, 2)
        self.ux_label_newClientName = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_newClientName.sizePolicy().hasHeightForWidth())
        self.ux_label_newClientName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_newClientName.setFont(font)
        self.ux_label_newClientName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ux_label_newClientName.setObjectName("ux_label_newClientName")
        self.ui_layout_newOrder.addWidget(self.ux_label_newClientName, 2, 0, 1, 1)
        self.ux_label_newClientAddress_line1 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_newClientAddress_line1.sizePolicy().hasHeightForWidth())
        self.ux_label_newClientAddress_line1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_newClientAddress_line1.setFont(font)
        self.ux_label_newClientAddress_line1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ux_label_newClientAddress_line1.setObjectName("ux_label_newClientAddress_line1")
        self.ui_layout_newOrder.addWidget(self.ux_label_newClientAddress_line1, 5, 0, 1, 1)
        self.ux_lineEdit_newClientPhone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_lineEdit_newClientPhone.sizePolicy().hasHeightForWidth())
        self.ux_lineEdit_newClientPhone.setSizePolicy(sizePolicy)
        self.ux_lineEdit_newClientPhone.setMinimumSize(QtCore.QSize(200, 0))
        self.ux_lineEdit_newClientPhone.setObjectName("ux_lineEdit_newClientPhone")
        self.ui_layout_newOrder.addWidget(self.ux_lineEdit_newClientPhone, 7, 1, 1, 2)
        self.ui_label_addNewClientHeader = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_addNewClientHeader.sizePolicy().hasHeightForWidth())
        self.ui_label_addNewClientHeader.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.ui_label_addNewClientHeader.setFont(font)
        self.ui_label_addNewClientHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_label_addNewClientHeader.setObjectName("ui_label_addNewClientHeader")
        self.ui_layout_newOrder.addWidget(self.ui_label_addNewClientHeader, 0, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui_layout_newOrder.addItem(spacerItem1, 12, 1, 1, 1)
        self.ux_label_newClientEmail = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_newClientEmail.sizePolicy().hasHeightForWidth())
        self.ux_label_newClientEmail.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_newClientEmail.setFont(font)
        self.ux_label_newClientEmail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ux_label_newClientEmail.setObjectName("ux_label_newClientEmail")
        self.ui_layout_newOrder.addWidget(self.ux_label_newClientEmail, 8, 0, 1, 1)
        self.ux_lineEdit_newClientEmail = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_lineEdit_newClientEmail.sizePolicy().hasHeightForWidth())
        self.ux_lineEdit_newClientEmail.setSizePolicy(sizePolicy)
        self.ux_lineEdit_newClientEmail.setMinimumSize(QtCore.QSize(200, 0))
        self.ux_lineEdit_newClientEmail.setObjectName("ux_lineEdit_newClientEmail")
        self.ui_layout_newOrder.addWidget(self.ux_lineEdit_newClientEmail, 8, 1, 1, 2)
        self.ui_layout_dynamicMainView.addLayout(self.ui_layout_newOrder, 0, 0, 1, 1)
        self.ux_pButton_newClient = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_newClient.setGeometry(QtCore.QRect(130, 120, 161, 61))
        self.ux_pButton_newClient.setObjectName("ux_pButton_newClient")
        self.ux_pButton_editClient = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_editClient.setGeometry(QtCore.QRect(130, 180, 161, 60))
        self.ux_pButton_editClient.setObjectName("ux_pButton_editClient")
        self.ux_pButton_addProduct = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_addProduct.setGeometry(QtCore.QRect(130, 240, 161, 61))
        self.ux_pButton_addProduct.setObjectName("ux_pButton_addProduct")
        self.ux_pButton_editProduct = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_editProduct.setGeometry(QtCore.QRect(130, 300, 161, 61))
        self.ux_pButton_editProduct.setObjectName("ux_pButton_editProduct")
        self.ux_pButton_newInvoice = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_newInvoice.setGeometry(QtCore.QRect(130, 360, 161, 41))
        self.ux_pButton_newInvoice.setObjectName("ux_pButton_newInvoice")
        self.ux_pButton_sendInvoice = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_sendInvoice.setGeometry(QtCore.QRect(130, 400, 161, 41))
        self.ux_pButton_sendInvoice.setObjectName("ux_pButton_sendInvoice")
        self.ux_pButton_searchInvoice = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_searchInvoice.setGeometry(QtCore.QRect(130, 440, 161, 41))
        self.ux_pButton_searchInvoice.setObjectName("ux_pButton_searchInvoice")
        self.ux_pButton_summaryView = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_summaryView.setGeometry(QtCore.QRect(130, 480, 161, 61))
        self.ux_pButton_summaryView.setObjectName("ux_pButton_summaryView")
        self.ux_pButton_searchView = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_searchView.setGeometry(QtCore.QRect(130, 540, 161, 61))
        self.ux_pButton_searchView.setObjectName("ux_pButton_searchView")
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
        self.ux_pButton_searchEditOrders.setText(_translate("MainWindow_mainView", "Search/Edit Orders"))
        self.ux_pButton_newOrder.setText(_translate("MainWindow_mainView", "New Order"))
        self.ux_label_newClientAddress_line2.setText(_translate("MainWindow_mainView", "Client City Code and City:"))
        self.ux_pButton_addClient.setText(_translate("MainWindow_mainView", "Add New Client"))
        self.ux_label_newClientPhone.setText(_translate("MainWindow_mainView", "Client Phone Number:"))
        self.ux_label_newClientName.setText(_translate("MainWindow_mainView", "Client Name:"))
        self.ux_label_newClientAddress_line1.setText(_translate("MainWindow_mainView", "Client Street Address:"))
        self.ui_label_addNewClientHeader.setText(_translate("MainWindow_mainView", "Add New Client"))
        self.ux_label_newClientEmail.setText(_translate("MainWindow_mainView", "Client Email Address:"))
        self.ux_pButton_newClient.setText(_translate("MainWindow_mainView", "Add New Client"))
        self.ux_pButton_editClient.setText(_translate("MainWindow_mainView", "Search/Edit Client Info."))
        self.ux_pButton_addProduct.setText(_translate("MainWindow_mainView", "Add New Product"))
        self.ux_pButton_editProduct.setText(_translate("MainWindow_mainView", "Search/Edit Product Info."))
        self.ux_pButton_newInvoice.setText(_translate("MainWindow_mainView", "Create New Invoice"))
        self.ux_pButton_sendInvoice.setText(_translate("MainWindow_mainView", "Send Invoice(s)"))
        self.ux_pButton_searchInvoice.setText(_translate("MainWindow_mainView", "Search Invoices"))
        self.ux_pButton_summaryView.setText(_translate("MainWindow_mainView", "Summary View"))
        self.ux_pButton_searchView.setText(_translate("MainWindow_mainView", "Search and View"))
