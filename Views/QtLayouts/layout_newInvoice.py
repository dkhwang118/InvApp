# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_newInvoice.ui'
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
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(310, 20, 871, 683))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ui_layout_dynamicMainView = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ui_layout_dynamicMainView.setContentsMargins(0, 0, 0, 0)
        self.ui_layout_dynamicMainView.setObjectName("ui_layout_dynamicMainView")
        self.ui_layout_searchEditClients = QtWidgets.QGridLayout()
        self.ui_layout_searchEditClients.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.ui_layout_searchEditClients.setSpacing(6)
        self.ui_layout_searchEditClients.setObjectName("ui_layout_searchEditClients")
        self.ui_label_newInvoice_orderNumber = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_orderNumber.setObjectName("ui_label_newInvoice_orderNumber")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_orderNumber, 17, 3, 1, 1)
        self.ux_lineEdit_newInvoice_orderSubTotal = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_orderSubTotal.setObjectName("ux_lineEdit_newInvoice_orderSubTotal")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_orderSubTotal, 19, 5, 1, 1)
        self.ui_label_newInvoice_orderSubTotal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_orderSubTotal.setObjectName("ui_label_newInvoice_orderSubTotal")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_orderSubTotal, 19, 3, 1, 1)
        self.ui_label_newInvoice_doubleClickTo_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_newInvoice_doubleClickTo_2.sizePolicy().hasHeightForWidth())
        self.ui_label_newInvoice_doubleClickTo_2.setSizePolicy(sizePolicy)
        self.ui_label_newInvoice_doubleClickTo_2.setObjectName("ui_label_newInvoice_doubleClickTo_2")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_doubleClickTo_2, 16, 1, 1, 1)
        self.ui_label_newInvoice_doubleClickTo = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_newInvoice_doubleClickTo.sizePolicy().hasHeightForWidth())
        self.ui_label_newInvoice_doubleClickTo.setSizePolicy(sizePolicy)
        self.ui_label_newInvoice_doubleClickTo.setObjectName("ui_label_newInvoice_doubleClickTo")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_doubleClickTo, 5, 1, 1, 1)
        self.ux_lineEdit_newInvoice_clientNameSearch = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_clientNameSearch.setObjectName("ux_lineEdit_newInvoice_clientNameSearch")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_clientNameSearch, 3, 1, 1, 1)
        self.ui_label_newInvoice_clientEmail = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_clientEmail.setObjectName("ui_label_newInvoice_clientEmail")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_clientEmail, 12, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui_layout_searchEditClients.addItem(spacerItem, 0, 0, 1, 1)
        self.ui_label_newInvoice_addressLine1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_addressLine1.setObjectName("ui_label_newInvoice_addressLine1")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_addressLine1, 9, 3, 1, 1)
        self.ui_label_newInvoice_addressLine2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_addressLine2.setObjectName("ui_label_newInvoice_addressLine2")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_addressLine2, 10, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ui_layout_searchEditClients.addItem(spacerItem1, 1, 2, 1, 1)
        self.ui_label_newInvoice_typeBelow = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_newInvoice_typeBelow.sizePolicy().hasHeightForWidth())
        self.ui_label_newInvoice_typeBelow.setSizePolicy(sizePolicy)
        self.ui_label_newInvoice_typeBelow.setObjectName("ui_label_newInvoice_typeBelow")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_typeBelow, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ui_layout_searchEditClients.addItem(spacerItem2, 8, 6, 1, 1)
        self.ui_label_newInvoice_header = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_newInvoice_header.sizePolicy().hasHeightForWidth())
        self.ui_label_newInvoice_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.ui_label_newInvoice_header.setFont(font)
        self.ui_label_newInvoice_header.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_label_newInvoice_header.setObjectName("ui_label_newInvoice_header")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_header, 0, 1, 1, 5)
        self.ux_pButton_newInvoice_showAllOrders = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ux_pButton_newInvoice_showAllOrders.setObjectName("ux_pButton_newInvoice_showAllOrders")
        self.ui_layout_searchEditClients.addWidget(self.ux_pButton_newInvoice_showAllOrders, 23, 1, 1, 1)
        self.ux_lineEdit_newInvoice_orderNumber = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_orderNumber.setObjectName("ux_lineEdit_newInvoice_orderNumber")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_orderNumber, 17, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui_layout_searchEditClients.addItem(spacerItem3, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui_layout_searchEditClients.addItem(spacerItem4, 8, 4, 1, 1)
        self.ux_lineEdit_newInvoice_cNameOut = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_cNameOut.setObjectName("ux_lineEdit_newInvoice_cNameOut")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_cNameOut, 8, 5, 1, 1)
        self.ui_label_newInvoice_clientPhone = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_clientPhone.setObjectName("ui_label_newInvoice_clientPhone")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_clientPhone, 11, 3, 1, 1)
        self.ux_lineEdit_newInvoice_address1Out = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_address1Out.setObjectName("ux_lineEdit_newInvoice_address1Out")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_address1Out, 9, 5, 1, 1)
        self.ux_lineEdit_newInvoice_address2Out = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_address2Out.setObjectName("ux_lineEdit_newInvoice_address2Out")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_address2Out, 10, 5, 1, 1)
        self.ux_lineEdit_newInvoice_cEmailOut = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_cEmailOut.setObjectName("ux_lineEdit_newInvoice_cEmailOut")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_cEmailOut, 12, 5, 1, 1)
        self.ux_lineEdit_newInvoice_cPhoneOut = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_cPhoneOut.setObjectName("ux_lineEdit_newInvoice_cPhoneOut")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_cPhoneOut, 11, 5, 1, 1)
        self.ui_label_newInvoice_taxApplied = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_taxApplied.setObjectName("ui_label_newInvoice_taxApplied")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_taxApplied, 20, 3, 1, 1)
        self.ui_label_newInvoice_orderTotal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_orderTotal.setObjectName("ui_label_newInvoice_orderTotal")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_orderTotal, 21, 3, 1, 1)
        self.ux_lineEdit_newInvoice_taxApplied = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_taxApplied.setObjectName("ux_lineEdit_newInvoice_taxApplied")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_taxApplied, 20, 5, 1, 1)
        self.ui_ListView_newInvoice_orderSearchList = QtWidgets.QListView(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_ListView_newInvoice_orderSearchList.sizePolicy().hasHeightForWidth())
        self.ui_ListView_newInvoice_orderSearchList.setSizePolicy(sizePolicy)
        self.ui_ListView_newInvoice_orderSearchList.setObjectName("ui_ListView_newInvoice_orderSearchList")
        self.ui_layout_searchEditClients.addWidget(self.ui_ListView_newInvoice_orderSearchList, 17, 1, 5, 1)
        self.ui_label_newInvoice_clientName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_clientName.setObjectName("ui_label_newInvoice_clientName")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_clientName, 8, 3, 1, 1)
        self.ui_label_newInvoice_orderItems = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ui_label_newInvoice_orderItems.setObjectName("ui_label_newInvoice_orderItems")
        self.ui_layout_searchEditClients.addWidget(self.ui_label_newInvoice_orderItems, 18, 3, 1, 1)
        self.ui_ListView_newInvoice_nameSearchList = QtWidgets.QListView(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_ListView_newInvoice_nameSearchList.sizePolicy().hasHeightForWidth())
        self.ui_ListView_newInvoice_nameSearchList.setSizePolicy(sizePolicy)
        self.ui_ListView_newInvoice_nameSearchList.setObjectName("ui_ListView_newInvoice_nameSearchList")
        self.ui_layout_searchEditClients.addWidget(self.ui_ListView_newInvoice_nameSearchList, 8, 1, 5, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui_layout_searchEditClients.addItem(spacerItem5, 25, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ui_layout_searchEditClients.addItem(spacerItem6, 13, 1, 3, 1)
        self.ux_pButton_newInvoice_ShowUnpaidOrders = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ux_pButton_newInvoice_ShowUnpaidOrders.setObjectName("ux_pButton_newInvoice_ShowUnpaidOrders")
        self.ui_layout_searchEditClients.addWidget(self.ux_pButton_newInvoice_ShowUnpaidOrders, 22, 1, 1, 1)
        self.ui_tableView_newInvoice_orderItems = QtWidgets.QTableView(self.gridLayoutWidget)
        self.ui_tableView_newInvoice_orderItems.setObjectName("ui_tableView_newInvoice_orderItems")
        self.ui_layout_searchEditClients.addWidget(self.ui_tableView_newInvoice_orderItems, 18, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ui_layout_searchEditClients.addItem(spacerItem7, 24, 1, 1, 1)
        self.ux_lineEdit_newInvoice_orderTotal = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ux_lineEdit_newInvoice_orderTotal.setObjectName("ux_lineEdit_newInvoice_orderTotal")
        self.ui_layout_searchEditClients.addWidget(self.ux_lineEdit_newInvoice_orderTotal, 21, 5, 1, 1)
        self.ux_pButton_newInvoice_createInvoice = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ux_pButton_newInvoice_createInvoice.setObjectName("ux_pButton_newInvoice_createInvoice")
        self.ui_layout_searchEditClients.addWidget(self.ux_pButton_newInvoice_createInvoice, 22, 5, 1, 1)
        self.ux_pButton_newInvoice_createAndSendInvoice = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ux_pButton_newInvoice_createAndSendInvoice.setObjectName("ux_pButton_newInvoice_createAndSendInvoice")
        self.ui_layout_searchEditClients.addWidget(self.ux_pButton_newInvoice_createAndSendInvoice, 23, 5, 1, 1)
        self.ui_layout_dynamicMainView.addLayout(self.ui_layout_searchEditClients, 1, 0, 1, 1)
        MainWindow_mainView.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_mainView)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_mainView)

    def retranslateUi(self, MainWindow_mainView):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_mainView.setWindowTitle(_translate("MainWindow_mainView", "MainWindow"))
        self.ui_label_newInvoice_orderNumber.setText(_translate("MainWindow_mainView", "Order Number:"))
        self.ui_label_newInvoice_orderSubTotal.setText(_translate("MainWindow_mainView", "Order SubTotal:"))
        self.ui_label_newInvoice_doubleClickTo_2.setText(_translate("MainWindow_mainView", "Double-Click on an Order Number to Show Orders Details:"))
        self.ui_label_newInvoice_doubleClickTo.setText(_translate("MainWindow_mainView", "Double-Click on Client Name Below to Show Client Orders:"))
        self.ui_label_newInvoice_clientEmail.setText(_translate("MainWindow_mainView", "Client Email:"))
        self.ui_label_newInvoice_addressLine1.setText(_translate("MainWindow_mainView", "Client Address Line 1:"))
        self.ui_label_newInvoice_addressLine2.setText(_translate("MainWindow_mainView", "Client Address Line 2:"))
        self.ui_label_newInvoice_typeBelow.setText(_translate("MainWindow_mainView", "Type a Client Name Below to Search:"))
        self.ui_label_newInvoice_header.setText(_translate("MainWindow_mainView", "Create New Invoice"))
        self.ux_pButton_newInvoice_showAllOrders.setText(_translate("MainWindow_mainView", "Show All Orders"))
        self.ui_label_newInvoice_clientPhone.setText(_translate("MainWindow_mainView", "Client Phone:"))
        self.ui_label_newInvoice_taxApplied.setText(_translate("MainWindow_mainView", "Tax Applied (in %):"))
        self.ui_label_newInvoice_orderTotal.setText(_translate("MainWindow_mainView", "Order Total:"))
        self.ui_label_newInvoice_clientName.setText(_translate("MainWindow_mainView", "Client Name:"))
        self.ui_label_newInvoice_orderItems.setText(_translate("MainWindow_mainView", "Order Items:"))
        self.ux_pButton_newInvoice_ShowUnpaidOrders.setText(_translate("MainWindow_mainView", "Show Unpaid Orders"))
        self.ux_pButton_newInvoice_createInvoice.setText(_translate("MainWindow_mainView", "Create Invoice"))
        self.ux_pButton_newInvoice_createAndSendInvoice.setText(_translate("MainWindow_mainView", "Create And Send Invoice"))
