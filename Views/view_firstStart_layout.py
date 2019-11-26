# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_view_firstStart.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartPage(object):
    def setupUi(self, ui_StartPage, firstTimeStartup):
        ui_StartPage.setObjectName("ui_StartPage")
        ui_StartPage.resize(1080, 310)
        self.centralwidget = QtWidgets.QWidget(ui_StartPage)
        self.centralwidget.setObjectName("centralwidget")
        self.startPage_stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.startPage_stackedWidget.setGeometry(QtCore.QRect(0, 0, 1080, 200))
        self.startPage_stackedWidget.setObjectName("startPage_stackedWidget")
        self.startPage_widget_FirstTimeStartup = QtWidgets.QWidget()
        self.startPage_widget_FirstTimeStartup.setObjectName("startPage_widget_FirstTimeStartup")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.startPage_widget_FirstTimeStartup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1081, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ui_vLayout_firstTimeStartup = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ui_vLayout_firstTimeStartup.setContentsMargins(0, 0, 0, 0)
        self.ui_vLayout_firstTimeStartup.setObjectName("ui_vLayout_firstTimeStartup")
        self.ui_label_firstTimeWelcome = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_firstTimeWelcome.sizePolicy().hasHeightForWidth())
        self.ui_label_firstTimeWelcome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.ui_label_firstTimeWelcome.setFont(font)
        self.ui_label_firstTimeWelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_label_firstTimeWelcome.setObjectName("ui_label_firstTimeWelcome")
        self.ui_vLayout_firstTimeStartup.addWidget(self.ui_label_firstTimeWelcome)
        self.ui_label_firstTimeText = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui_label_firstTimeText.setFont(font)
        self.ui_label_firstTimeText.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_label_firstTimeText.setObjectName("ui_label_firstTimeText")
        self.ui_vLayout_firstTimeStartup.addWidget(self.ui_label_firstTimeText)
        self.startPage_stackedWidget.addWidget(self.startPage_widget_FirstTimeStartup)

        # define widget for welcome screen when not the first application initialization
        self.startPage_widget_welcomeScreen = QtWidgets.QWidget()
        self.startPage_widget_welcomeScreen.setObjectName("startPage_widget_welcomeScreen")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.startPage_widget_welcomeScreen)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 1081, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.ui_vLayout_welcomeScreen = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.ui_vLayout_welcomeScreen.setContentsMargins(0, 0, 0, 0)
        self.ui_vLayout_welcomeScreen.setObjectName("ui_vLayout_welcomeScreen")
        self.ui_label_welcomeScreen = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.ui_label_welcomeScreen.setFont(font)
        self.ui_label_welcomeScreen.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_label_welcomeScreen.setObjectName("ui_label_welcomeScreen")
        self.ui_vLayout_welcomeScreen.addWidget(self.ui_label_welcomeScreen)
        self.ui_label_passwordText = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ui_label_passwordText.setFont(font)
        self.ui_label_passwordText.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_label_passwordText.setObjectName("ui_label_passwordText")
        self.ui_vLayout_welcomeScreen.addWidget(self.ui_label_passwordText)
        self.startPage_stackedWidget.addWidget(self.startPage_widget_welcomeScreen)
        self.ux_lineEdit_passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ux_lineEdit_passwordInput.setGeometry(QtCore.QRect(440, 230, 291, 20))
        self.ux_lineEdit_passwordInput.setObjectName("ux_lineEdit_passwordInput")
        self.ui_label_password = QtWidgets.QLabel(self.centralwidget)
        self.ui_label_password.setGeometry(QtCore.QRect(360, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ui_label_password.setFont(font)
        self.ui_label_password.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_label_password.setObjectName("ui_label_password")
        self.ux_pButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.ux_pButton_login.setGeometry(QtCore.QRect(510, 260, 131, 41))
        self.ux_pButton_login.setObjectName("ux_pButton_login")
        self.ux_pButton_login.setAutoDefault(True)
        ui_StartPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(ui_StartPage)

        # set widget according to firstTimeStartup param
        if firstTimeStartup:
            self.startPage_stackedWidget.setCurrentWidget(self.startPage_widget_FirstTimeStartup)
        else:
            self.startPage_stackedWidget.setCurrentWidget(self.startPage_widget_welcomeScreen)

        QtCore.QMetaObject.connectSlotsByName(ui_StartPage)

    def retranslateUi(self, ui_StartPage):
        _translate = QtCore.QCoreApplication.translate
        ui_StartPage.setWindowTitle(_translate("ui_StartPage", "MainWindow"))
        self.ui_label_firstTimeWelcome.setText(_translate("ui_StartPage", "Welcome to the Invoice and Order Management Application!"))
        self.ui_label_firstTimeText.setText(_translate("ui_StartPage", "Since this is the first time opening the application, please type in a password below to ensure your data is secure. "))
        self.ui_label_welcomeScreen.setText(_translate("ui_StartPage", "Welcome Back to the Invoice and Order Management Application!"))
        self.ui_label_passwordText.setText(_translate("ui_StartPage", "Please login by inputting your password below."))
        self.ui_label_password.setText(_translate("ui_StartPage", "Password:"))
        self.ux_pButton_login.setText(_translate("ui_StartPage", "Login"))
