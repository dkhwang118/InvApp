# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Views\view_main_ui_v2base.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_mainView(object):
    def setupUi(self, main_view):

        # init main window
        main_view.setObjectName("main_view")
        main_view.resize(1200, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_view.sizePolicy().hasHeightForWidth())
        main_view.setSizePolicy(sizePolicy)

        # init top-level QWidget in main window
        self.centralwidget = QtWidgets.QWidget(main_view)
        self.centralwidget.setObjectName("centralwidget")

        # init QWidget holding the left-most vertical layout
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 131, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        # init left-most vertical layout (holds left buttons)
        self.ui_vLayout_viewMain = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ui_vLayout_viewMain.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.ui_vLayout_viewMain.setContentsMargins(0, 0, 0, 0)
        self.ui_vLayout_viewMain.setSpacing(0)
        self.ui_vLayout_viewMain.setObjectName("ui_vLayout_viewMain")

        # init buttons within ui_vLayout_viewMain
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

        # init 2nd level buttons (e.g. New Orders)
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


        # init stacked layout widget
        self.stackedLayoutWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedLayoutWidget.setGeometry(QtCore.QRect(290, 0, 911, 721))
        self.stackedLayoutWidget.setObjectName("welcomeLayoutWidget")

        # init welcome window widget
        self.welcomeLayoutWidget = QtWidgets.QWidget(self.stackedLayoutWidget)
        self.welcomeLayoutWidget.setGeometry(QtCore.QRect(290, 0, 911, 721))
        self.welcomeLayoutWidget.setObjectName("welcomeLayoutWidget")

        self.ui_layout_welcomePage = QtWidgets.QGridLayout()
        self.ui_layout_welcomePage.setGeometry(QtCore.QRect(290, 0, 911, 721))
        self.ui_layout_welcomePage.setContentsMargins(0, 0, 0, 0)
        self.ui_layout_welcomePage.setObjectName("ui_layout_welcomePage")
        self.ux_label_welcome = QtWidgets.QLabel(self.welcomeLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ux_label_welcome.setFont(font)
        self.ux_label_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.ux_label_welcome.setObjectName("ux_label_welcome")
        self.ui_layout_welcomePage.addWidget(self.ux_label_welcome, 0, 0, 1, 1)



        self.welcomeLayoutWidget.setLayout(self.ui_layout_welcomePage)

        self.stackedLayoutWidget.addWidget(self.welcomeLayoutWidget)


        # # init welcome window widget
        # self.welcomeLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # self.welcomeLayoutWidget.setGeometry(QtCore.QRect(290, 0, 911, 721))
        # self.welcomeLayoutWidget.setObjectName("welcomeLayoutWidget")
        # self.ui_layout_dynamicMainView = QtWidgets.QGridLayout(self.welcomeLayoutWidget)
        # self.ui_layout_dynamicMainView.setContentsMargins(0, 0, 0, 0)
        # self.ui_layout_dynamicMainView.setObjectName("ui_layout_dynamicMainView")
        # self.ux_label_welcome = QtWidgets.QLabel(self.welcomeLayoutWidget)
        # font = QtGui.QFont()
        # font.setPointSize(24)
        # self.ux_label_welcome.setFont(font)
        # self.ux_label_welcome.setAlignment(QtCore.Qt.AlignCenter)
        # self.ux_label_welcome.setObjectName("ux_label_welcome")
        # self.ui_layout_dynamicMainView.addWidget(self.ux_label_welcome, 0, 0, 1, 1)

        main_view.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_view)
        QtCore.QMetaObject.connectSlotsByName(main_view)

    def retranslateUi(self, MainWindow_mainView):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_mainView.setWindowTitle(_translate("main_view", "MainWindow"))
        self.ux_pButton_orders.setText(_translate("main_view", "Orders"))
        self.ux_pButton_clients.setText(_translate("main_view", "Clients"))
        self.ux_pButton_products.setText(_translate("main_view", "Products"))
        self.ux_pButton_invoicing.setText(_translate("main_view", "Invoicing"))
        self.ux_pButton_statistics.setText(_translate("main_view", "Statistics"))
        self.ux_pButton_settings.setText(_translate("main_view", "Settings"))
        self.ux_pButton_searchEditOrders.setText(_translate("main_view", "Search/Edit Orders"))
        self.ux_pButton_newOrder.setText(_translate("main_view", "New Order"))
        self.ux_label_welcome.setText(_translate("main_view", "Welcome!"))
