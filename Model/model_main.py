###########################################################################
#
#   model_main.py
#   Original design framework by "101" and "Roberto Leinardi" (https://stackoverflow.com/a/26699122)
#   sqlite3 implementation framework by "Adam McQuistan" (https://stackabuse.com/a-sqlite-tutorial-with-python/)
#
#   Edited by: David K. Hwang
#
#
############################################################################

from PyQt5.QtCore import QObject, pyqtSignal
from Model.model_sql_db_utils import *


class Model(QObject):

    # define signals dependent on changes in model
    amount_changed = pyqtSignal(int)
    even_odd_changed = pyqtSignal(str)
    enable_reset_changed = pyqtSignal(bool)


    # define page-change signal
    mainView_changed = pyqtSignal(int)
    currentTier2Buttons_changed = pyqtSignal(int)

    # signal to tell view to show a QMessageBox with given string values (title, text)
    show_message_box = pyqtSignal(tuple)

    # signal to tell view whether last call was successful or not
    call_success = pyqtSignal(int)

    # signal to tell view about updated list values
    searchEditClients_searchClientNames_newValues = pyqtSignal(list)
    searchEditClients_clientInfoDoubleClick = pyqtSignal(str, str, str, str, str)

    # signal to tell view about changes in modes depedning on button press
    searchEditClients_editModeChanged = pyqtSignal(int)


    @property
    def currentView(self):
        return self._currentView

    @currentView.setter
    def currentView(self, value):
        self._currentView = value
        self.mainView_changed.emit(value)

    @property
    def searchEditClients_editMode(self):
        return self._searchEditClients_editMode

    @searchEditClients_editMode.setter
    def searchEditClients_editMode(self, value):
        self._searchEditClients_editMode = value
        self.searchEditClients_editModeChanged.emit(value)

    @property
    def currentClientId(self):
        return self._currentClientId

    @currentClientId.setter
    def currentClientId(self, value):
        self._currentClientId = value

    @property
    def currentTier2Buttons(self):
        return self._currentTier2Buttons

    @currentTier2Buttons.setter
    def currentTier2Buttons(self, value):
        self._currentTier2Buttons = value
        self.currentTier2Buttons_changed.emit(value)

    @property
    def message_box_values(self):
        return self._message_box_values

    @message_box_values.setter
    def message_box_values(self, value):
        self._message_box_values = value
        self.show_message_box.emit(value)

    @property
    def last_db_return_value(self):
        return self._last_db_return_value

    @last_db_return_value.setter
    def last_db_return_value(self, value):
        self._last_db_return_value = value
        self.call_success.emit(value)

    @property
    def firstTimeStartup(self):
        return self._firstTimeStartup

    @property
    def db_connection(self):
        return self._db_connection

    @db_connection.setter
    def db_connection(self, db_conn):
        self._db_connection = db_conn

    @property
    def db_cursor(self):
        return self._db_connection

    @db_cursor.setter
    def db_cursor(self, db_cur):
        self._db_cursor = db_cur

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amount_changed.emit(value)

    @property
    def even_odd(self):
        return self._even_odd

    @even_odd.setter
    def even_odd(self, value):
        self._even_odd = value
        self.even_odd_changed.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_changed.emit(value)


    def __init__(self):
        super().__init__()

        # on model init, check if database file exists
        if db_isPresent():
            self._firstTimeStartup = False
        else:
            self._firstTimeStartup = True

        # init _db_connection
        self._db_connection = None
        self._db_cursor = None

        # set current view for main window
        self._currentView = 0

        # set current visibility of Tier2 buttons
        self._currentTier2Buttons = 0

        self._message_box_values = ("", "")
        self._last_db_return_value = -1

        # set searchEditClient page signals and properties
        self._searchEditClients_editMode = 0

        # misc global propertes
        self._currentClientId = -1

        self._amount = 0
        self._even_odd = ''
        self._enable_reset = False

    # function to try given password
    def db_connection_init(self, db_pass):
        # start db connection based on if initial application launch or re-login
        if self._firstTimeStartup:
            self._db_connection, self._db_cursor = firstTimeCreate(db_pass)
        else:
            self._db_connection, self._db_cursor = create_connection(db_pass)

        # check to see if password was correct (if app is connected to db) and return boolean result
        return db_connectionCheck(self._db_connection)

    #######################################################################
    #
    #   Database functions to query and change data
    #
    #######################################################################

    ### function to add new clients to db
    def db_addNewClient(self, name, address1, address2, phone, email):
        return_val, title, text = addNewClient(self._db_connection, self._db_cursor, name, address1, address2, phone, email)
        db_printAllClients(self._db_connection)
        return return_val, title, text

    def getAllClients(self):
        db_cur = self._db_connection.cursor()
        db_cur.execute("SELECT Name, Id FROM Clients;")
        clientNameList = db_cur.fetchall()
        self.searchEditClients_searchClientNames_newValues.emit(clientNameList)
        return clientNameList

    def getAllClients_byName(self, name):
        db_cur = self._db_connection.cursor()
        formattedName = name + "%"
        db_cur.execute("SELECT Name, Id FROM Clients WHERE Name LIKE ?;", (formattedName,))
        self.searchEditClients_searchClientNames_newValues.emit(db_cur.fetchall())

    def getClientInfo_byId(self, id):
        db_cur = self._db_connection.cursor()
        db_cur.execute("SELECT * FROM Clients WHERE Id=?;", (str(id),))
        tempList = db_cur.fetchone()
        print(tempList)
        name = tempList[1]
        address1 = tempList[2]
        address2 = tempList[3]
        phone = tempList[4]
        email = tempList[5]
        self.searchEditClients_clientInfoDoubleClick.emit(name, address1, address2, phone, email)

