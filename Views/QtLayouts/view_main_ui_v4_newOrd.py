# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_main_ui_v4_newOrd.ui'
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
        self.ux_pButton_revAndComp = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ux_pButton_revAndComp.setMinimumSize(QtCore.QSize(0, 50))
        self.ux_pButton_revAndComp.setObjectName("ux_pButton_revAndComp")
        self.ui_layout_newOrder.addWidget(self.ux_pButton_revAndComp, 15, 4, 1, 1)
        self.ux_pButton_addProdToOrd = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_pButton_addProdToOrd.sizePolicy().hasHeightForWidth())
        self.ux_pButton_addProdToOrd.setSizePolicy(sizePolicy)
        self.ux_pButton_addProdToOrd.setMinimumSize(QtCore.QSize(280, 0))
        self.ux_pButton_addProdToOrd.setObjectName("ux_pButton_addProdToOrd")
        self.ui_layout_newOrder.addWidget(self.ux_pButton_addProdToOrd, 13, 0, 1, 1)
        self.ux_tableWidget_curProducts = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_tableWidget_curProducts.sizePolicy().hasHeightForWidth())
        self.ux_tableWidget_curProducts.setSizePolicy(sizePolicy)
        self.ux_tableWidget_curProducts.setMinimumSize(QtCore.QSize(290, 0))
        self.ux_tableWidget_curProducts.setShowGrid(True)
        self.ux_tableWidget_curProducts.setRowCount(0)
        self.ux_tableWidget_curProducts.setColumnCount(2)
        self.ux_tableWidget_curProducts.setObjectName("ux_tableWidget_curProducts")
        item = QtWidgets.QTableWidgetItem()
        self.ux_tableWidget_curProducts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ux_tableWidget_curProducts.setHorizontalHeaderItem(1, item)
        self.ux_tableWidget_curProducts.horizontalHeader().setCascadingSectionResizes(False)
        self.ux_tableWidget_curProducts.horizontalHeader().setDefaultSectionSize(140)
        self.ux_tableWidget_curProducts.verticalHeader().setVisible(False)
        self.ui_layout_newOrder.addWidget(self.ux_tableWidget_curProducts, 12, 0, 1, 1)
        self.ux_label_deliveryDate = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_deliveryDate.sizePolicy().hasHeightForWidth())
        self.ux_label_deliveryDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_deliveryDate.setFont(font)
        self.ux_label_deliveryDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ux_label_deliveryDate.setObjectName("ux_label_deliveryDate")
        self.ui_layout_newOrder.addWidget(self.ux_label_deliveryDate, 4, 0, 1, 1)
        self.ux_label_clientName = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_clientName.sizePolicy().hasHeightForWidth())
        self.ux_label_clientName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_clientName.setFont(font)
        self.ux_label_clientName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ux_label_clientName.setObjectName("ux_label_clientName")
        self.ui_layout_newOrder.addWidget(self.ux_label_clientName, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ui_layout_newOrder.addItem(spacerItem, 5, 2, 1, 1)
        self.ux_label_orderNumber = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_orderNumber.sizePolicy().hasHeightForWidth())
        self.ux_label_orderNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_orderNumber.setFont(font)
        self.ux_label_orderNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ux_label_orderNumber.setObjectName("ux_label_orderNumber")
        self.ui_layout_newOrder.addWidget(self.ux_label_orderNumber, 0, 0, 1, 1)
        self.ux_label_selectProd = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_label_selectProd.sizePolicy().hasHeightForWidth())
        self.ux_label_selectProd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_selectProd.setFont(font)
        self.ux_label_selectProd.setAlignment(QtCore.Qt.AlignCenter)
        self.ux_label_selectProd.setObjectName("ux_label_selectProd")
        self.ui_layout_newOrder.addWidget(self.ux_label_selectProd, 11, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ui_layout_newOrder.addItem(spacerItem1, 14, 4, 1, 1)
        self.ux_tableWidget_orderProducts = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_tableWidget_orderProducts.sizePolicy().hasHeightForWidth())
        self.ux_tableWidget_orderProducts.setSizePolicy(sizePolicy)
        self.ux_tableWidget_orderProducts.setShowGrid(True)
        self.ux_tableWidget_orderProducts.setRowCount(0)
        self.ux_tableWidget_orderProducts.setColumnCount(4)
        self.ux_tableWidget_orderProducts.setObjectName("ux_tableWidget_orderProducts")
        item = QtWidgets.QTableWidgetItem()
        self.ux_tableWidget_orderProducts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ux_tableWidget_orderProducts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ux_tableWidget_orderProducts.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ux_tableWidget_orderProducts.setHorizontalHeaderItem(3, item)
        self.ux_tableWidget_orderProducts.horizontalHeader().setDefaultSectionSize(120)
        self.ui_layout_newOrder.addWidget(self.ux_tableWidget_orderProducts, 12, 2, 1, 3)
        self.ux_label_prodInCurOrder = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ux_label_prodInCurOrder.setFont(font)
        self.ux_label_prodInCurOrder.setAlignment(QtCore.Qt.AlignCenter)
        self.ux_label_prodInCurOrder.setObjectName("ux_label_prodInCurOrder")
        self.ui_layout_newOrder.addWidget(self.ux_label_prodInCurOrder, 11, 2, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui_layout_newOrder.addItem(spacerItem2, 12, 1, 1, 1)
        self.ux_lineEdit_deliveryDate = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_lineEdit_deliveryDate.sizePolicy().hasHeightForWidth())
        self.ux_lineEdit_deliveryDate.setSizePolicy(sizePolicy)
        self.ux_lineEdit_deliveryDate.setMinimumSize(QtCore.QSize(200, 0))
        self.ux_lineEdit_deliveryDate.setObjectName("ux_lineEdit_deliveryDate")
        self.ui_layout_newOrder.addWidget(self.ux_lineEdit_deliveryDate, 4, 1, 1, 2)
        self.ux_comboBox_clientName = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_comboBox_clientName.sizePolicy().hasHeightForWidth())
        self.ux_comboBox_clientName.setSizePolicy(sizePolicy)
        self.ux_comboBox_clientName.setMinimumSize(QtCore.QSize(200, 0))
        self.ux_comboBox_clientName.setObjectName("ux_comboBox_clientName")
        self.ui_layout_newOrder.addWidget(self.ux_comboBox_clientName, 1, 1, 1, 2)
        self.ux_lineEdit_orderNumber = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ux_lineEdit_orderNumber.sizePolicy().hasHeightForWidth())
        self.ux_lineEdit_orderNumber.setSizePolicy(sizePolicy)
        self.ux_lineEdit_orderNumber.setMinimumSize(QtCore.QSize(200, 0))
        self.ux_lineEdit_orderNumber.setObjectName("ux_lineEdit_orderNumber")
        self.ui_layout_newOrder.addWidget(self.ux_lineEdit_orderNumber, 0, 1, 1, 2)
        self.ux_pButton_compOrder = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ux_pButton_compOrder.setObjectName("ux_pButton_compOrder")
        self.ui_layout_newOrder.addWidget(self.ux_pButton_compOrder, 13, 2, 1, 3)
        self.ui_layout_dynamicMainView.addLayout(self.ui_layout_newOrder, 0, 0, 1, 1)
        self.ux_pButton_newClient = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_newClient.setGeometry(QtCore.QRect(130, 120, 161, 61))
        self.ux_pButton_newClient.setObjectName("ux_pButton_newClient")
        self.ux_pButton_editClient = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_editClient.setGeometry(QtCore.QRect(130, 180, 161, 61))
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
        self.ux_pButton_revAndComp.setText(_translate("MainWindow_mainView", "Review and Complete Order"))
        self.ux_pButton_addProdToOrd.setText(_translate("MainWindow_mainView", "Add Product To Order"))
        item = self.ux_tableWidget_curProducts.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_mainView", "Product Name"))
        item = self.ux_tableWidget_curProducts.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_mainView", "Price-Per-Unit"))
        self.ux_label_deliveryDate.setText(_translate("MainWindow_mainView", "Delivery Date:"))
        self.ux_label_clientName.setText(_translate("MainWindow_mainView", "Client Name:"))
        self.ux_label_orderNumber.setText(_translate("MainWindow_mainView", "Facture/Order #:"))
        self.ux_label_selectProd.setText(_translate("MainWindow_mainView", "Select Products for Current Order:"))
        item = self.ux_tableWidget_orderProducts.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_mainView", "Product Name"))
        item = self.ux_tableWidget_orderProducts.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_mainView", "Unit Amount"))
        item = self.ux_tableWidget_orderProducts.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_mainView", "Price-Per-Unit"))
        item = self.ux_tableWidget_orderProducts.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_mainView", "Total Cost"))
        self.ux_label_prodInCurOrder.setText(_translate("MainWindow_mainView", "Products in Current Order:"))
        self.ux_pButton_compOrder.setText(_translate("MainWindow_mainView", "Remove Product From Order"))
        self.ux_pButton_newClient.setText(_translate("MainWindow_mainView", "Add New Client"))
        self.ux_pButton_editClient.setText(_translate("MainWindow_mainView", "Search/Edit Client Info."))
        self.ux_pButton_addProduct.setText(_translate("MainWindow_mainView", "Add New Product"))
        self.ux_pButton_editProduct.setText(_translate("MainWindow_mainView", "Search/Edit Product Info."))
        self.ux_pButton_newInvoice.setText(_translate("MainWindow_mainView", "Create New Invoice"))
        self.ux_pButton_sendInvoice.setText(_translate("MainWindow_mainView", "Send Invoice(s)"))
        self.ux_pButton_searchInvoice.setText(_translate("MainWindow_mainView", "Search Invoices"))
        self.ux_pButton_summaryView.setText(_translate("MainWindow_mainView", "Summary View"))
        self.ux_pButton_searchView.setText(_translate("MainWindow_mainView", "Search and View"))
