######################################################################################################################
#
#   view_SearchSelect_ClientByName
#
#   UI Qt Design Layout for a pop-up page that allows user to search for a client by name and select them
#
######################################################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt

class UI_SearchSelect_ClientbyName(object):
    def setupUi(self, ui_searchSelect_clientByName, model, main_controller):

        ui_searchSelect_clientByName.setObjectName("ui_searchSelect_clientByName")
        ui_searchSelect_clientByName.resize(900, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui_searchSelect_clientByName.sizePolicy().hasHeightForWidth())

        ui_searchSelect_clientByName.setSizePolicy(sizePolicy)
        ui_searchSelect_clientByName.setFixedSize(ui_searchSelect_clientByName.size())

        # set the grid layout widget for the window
        self.widget_layout_searchNamesPopup = QtWidgets.QWidget(ui_searchSelect_clientByName)
        self.widget_layout_searchNamesPopup.setGeometry(QtCore.QRect(0,0,900,450))
        self.widget_layout_searchNamesPopup.setObjectName("widget_layout_searchNamesPopup")

        # setup grid layout snapped to widget
        self.ui_gridLayout_searchNamesPopup = QtWidgets.QGridLayout()
        self.ui_gridLayout_searchNamesPopup.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ui_gridLayout_searchNamesPopup.setSpacing(6)
        self.ui_gridLayout_searchNamesPopup.setObjectName("ui_gridLayout_searchNamesPopup")


        ################################
        #   Search Grid
        ################################

        # ListView for current names on search list
        self.ui_ListView_searchNamesPopup_nameSearchList = QtWidgets.QListView(self.widget_layout_searchNamesPopup)
        self.ui_ListView_searchNamesPopup_nameSearchList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui_ListView_searchNamesPopup_nameSearchList.setMinimumSize(QtCore.QSize(360,0))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.ui_ListView_searchNamesPopup_nameSearchList.setSizePolicy(sizePolicy)
        self.ui_ListView_searchNamesPopup_nameSearchList.setObjectName("ui_ListView_searchEditClients_nameSearchList")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_ListView_searchNamesPopup_nameSearchList, 5, 1, 9, 1)



        # header for GridLayout
        self.ui_label_searchEditClients_header = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_searchEditClients_header.sizePolicy().hasHeightForWidth())
        self.ui_label_searchEditClients_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.ui_label_searchEditClients_header.setFont(font)
        self.ui_label_searchEditClients_header.setAlignment(QtCore.Qt.AlignCenter)
        self.ui_label_searchEditClients_header.setObjectName("ui_label_searchEditClients_header")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchEditClients_header, 0, 1, 1, 5)

        # LineEdit for user to type in names for Client Name search
        self.ux_lineEdit_searchEditClients_clientNameSearch = QtWidgets.QLineEdit(self.widget_layout_searchNamesPopup)
        self.ux_lineEdit_searchEditClients_clientNameSearch.setMinimumSize(QtCore.QSize(360, 0))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.ux_lineEdit_searchEditClients_clientNameSearch.setSizePolicy(sizePolicy)
        self.ux_lineEdit_searchEditClients_clientNameSearch.setObjectName(
            "ux_lineEdit_searchEditClients_clientNameSearch")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ux_lineEdit_searchEditClients_clientNameSearch, 3, 1, 1, 1)



        # spacers for Grid Layout

        # spacer to the left of the header label
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.ui_gridLayout_searchNamesPopup.addItem(spacerItem3, 0, 0, 1, 1)

        # spacer to the right of header label
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.ui_gridLayout_searchNamesPopup.addItem(spacerItem1, 0, 6, 1, 1)

        # spacer separating header label and rest of form
        spacerItem2 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.ui_gridLayout_searchNamesPopup.addItem(spacerItem2, 1, 2, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ui_gridLayout_searchNamesPopup.addItem(spacerItem, 13, 5, 1, 1)

        # spacer at the bottom of view
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.ui_gridLayout_searchNamesPopup.addItem(spacerItem4, 14, 1, 1, 1)

        # between left side of form and right side
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui_gridLayout_searchNamesPopup.addItem(spacerItem5, 3, 2, 1, 1)

        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui_gridLayout_searchNamesPopup.addItem(spacerItem6, 8, 4, 1, 1)

        # Label signaling user to type below it to start client name search
        self.ui_label_searchEditClients_typeBelow = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_searchEditClients_typeBelow.sizePolicy().hasHeightForWidth())
        self.ui_label_searchEditClients_typeBelow.setSizePolicy(sizePolicy)
        self.ui_label_searchEditClients_typeBelow.setObjectName("ui_label_searchEditClients_typeBelow")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchEditClients_typeBelow, 2, 1, 1, 1)



        # Label above ListView of client names, asking user to DoubleClick for more info
        self.ui_label_searchEditClients_doubleClickTo = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_label_searchEditClients_doubleClickTo.sizePolicy().hasHeightForWidth())
        self.ui_label_searchEditClients_doubleClickTo.setSizePolicy(sizePolicy)
        self.ui_label_searchEditClients_doubleClickTo.setObjectName("ui_label_searchEditClients_doubleClickTo")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchEditClients_doubleClickTo, 4, 1, 1, 1)


        # size policy to expand the right labels into the open center area
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # right-side label for "Client Name:"
        self.ui_label_searchClientsPopup_cNameLabel = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchClientsPopup_cNameLabel.setSizePolicy(sizePolicy)
        self.ui_label_searchClientsPopup_cNameLabel.setObjectName("ui_label_searchEditClients_clientName")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchClientsPopup_cNameLabel, 2, 3, 1, 1)

        self.ui_label_searchEditClients_addressLine1 = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchEditClients_addressLine1.setObjectName("ui_label_searchEditClients_addressLine1")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchEditClients_addressLine1, 4, 3, 1, 1)

        self.ui_label_searchEditClients_addressLine2 = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchEditClients_addressLine2.setObjectName("ui_label_searchEditClients_addressLine2")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchEditClients_addressLine2, 6, 3, 1, 1)

        self.ui_label_searchEditClients_clientPhone = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchEditClients_clientPhone.setObjectName("ui_label_searchEditClients_clientPhone")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchEditClients_clientPhone, 8, 3, 1, 1)

        # Label showing the current client's email address
        self.ui_label_searchEditClients_clientEmail = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchEditClients_clientEmail.setObjectName("ui_label_searchEditClients_clientEmail")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchEditClients_clientEmail, 10, 3, 1, 1)

        # Left-Side data showing name, address, etc. when user clicks on a name in the ListView
        self.ui_label_searchClientsPopup_cNameOut = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchClientsPopup_cNameOut.setAlignment(Qt.AlignCenter)
        self.ui_label_searchClientsPopup_cNameOut.setObjectName("ui_label_searchClientsPopup_cNameOut")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchClientsPopup_cNameOut, 3, 3, 1, 3)

        self.ui_label_searchClientsPopup_address1Out = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchClientsPopup_address1Out.setAlignment(Qt.AlignCenter)
        self.ui_label_searchClientsPopup_address1Out.setObjectName("ui_label_searchClientsPopup_address1Out")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchClientsPopup_address1Out, 5, 3, 1, 3)

        self.ui_label_searchClientsPopup_address2Out = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchClientsPopup_address2Out.setAlignment(Qt.AlignCenter)
        self.ui_label_searchClientsPopup_address2Out.setObjectName("ux_lineEdit_searchEditClients_address2Out")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchClientsPopup_address2Out, 7, 3, 1, 3)

        self.ui_label_searchClientsPopup_cPhoneOut = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchClientsPopup_cPhoneOut.setAlignment(Qt.AlignCenter)
        self.ui_label_searchClientsPopup_cPhoneOut.setObjectName("ui_label_searchClientsPopup_cPhoneOut")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchClientsPopup_cPhoneOut, 9, 3, 1, 3)

        self.ui_label_searchClientsPopup_cEmailOut = QtWidgets.QLabel(self.widget_layout_searchNamesPopup)
        self.ui_label_searchClientsPopup_cEmailOut.setAlignment(Qt.AlignCenter)
        self.ui_label_searchClientsPopup_cEmailOut.setObjectName("ui_label_searchClientsPopup_cEmailOut")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ui_label_searchClientsPopup_cEmailOut, 11, 3, 1, 3)


        # button user clicks to select currently selected Client
        self.ux_pButton_searchClientsPopup_SelectClient = QtWidgets.QPushButton(self.widget_layout_searchNamesPopup)
        self.ux_pButton_searchClientsPopup_SelectClient.setObjectName("ux_pButton_searchClientsPopup_SelectClient")
        self.ui_gridLayout_searchNamesPopup.addWidget(self.ux_pButton_searchClientsPopup_SelectClient, 13, 3, 1, 3)

        self.ui_gridLayout_searchNamesPopup.addLayout(self.ui_gridLayout_searchNamesPopup, 1, 0, 1, 1)

        self.widget_layout_searchNamesPopup.setLayout(self.ui_gridLayout_searchNamesPopup)

        self.retranslateUi(ui_searchSelect_clientByName)
        QtCore.QMetaObject.connectSlotsByName(ui_searchSelect_clientByName)

    def retranslateUi(self, ui_searchSelect_clientByName):
        _translate = QtCore.QCoreApplication.translate
        ui_searchSelect_clientByName.setWindowTitle(_translate("ui_searchSelect_clientByName", "Select A Client ..."))
        self.ui_label_searchEditClients_header.setText(
            _translate("ui_searchSelect_clientByName", "Select A Client ..."))
        self.ui_label_searchEditClients_typeBelow.setText(
            _translate("ui_searchSelect_clientByName", "Type a Clent Name Below to Search:"))
        self.ui_label_searchEditClients_clientEmail.setText(_translate("ui_searchSelect_clientByName", "Email:"))
        self.ui_label_searchEditClients_doubleClickTo.setText(
            _translate("ui_searchSelect_clientByName", "Double-Click on Client Name Below to Show Information:"))
        self.ui_label_searchClientsPopup_cNameLabel.setText(_translate("ui_searchSelect_clientByName", "Name:"))
        self.ui_label_searchEditClients_addressLine2.setText(
            _translate("ui_searchSelect_clientByName", "Address Line 2:"))
        self.ui_label_searchEditClients_addressLine1.setText(
            _translate("ui_searchSelect_clientByName", "Address Line 1:"))
        self.ui_label_searchEditClients_clientPhone.setText(_translate("ui_searchSelect_clientByName", "Phone:"))
        # self.ux_pButton_searchEditClients_editClientInfo.setText(
        #     _translate("ui_searchSelect_clientByName", "Edit Client Information"))
        self.ux_pButton_searchClientsPopup_SelectClient.setText(
            _translate("ui_searchSelect_clientByName", "Select Client"))

        self.ui_label_searchClientsPopup_cNameOut.setText(_translate("ui_searchSelect_clientByName",
                                                                     "Select Client to see Name ..."))
        self.ui_label_searchClientsPopup_address1Out.setText(_translate("ui_searchSelect_clientByName",
                                                                     "Select Client to see Address ..."))
        self.ui_label_searchClientsPopup_address2Out.setText(_translate("ui_searchSelect_clientByName",
                                                                     "Select Client to see Address ..."))
        self.ui_label_searchClientsPopup_cPhoneOut.setText(_translate("ui_searchSelect_clientByName",
                                                                     "Select Client to see Phone Number ..."))
        self.ui_label_searchClientsPopup_cEmailOut.setText(_translate("ui_searchSelect_clientByName",
                                                                     "Select Client to see Email Address ..."))