# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\View.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import  Error
import mysql.connector
class Ui_MainWindow(object):
    def load(self):
        database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='lyrics')
        cursor = database.cursor()
        cursor.execute("select *from dataset")
        row = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(row):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
              self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 471, 192))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.view = QtWidgets.QPushButton(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(190, 220, 75, 23))
        self.view.setObjectName("view")
        self.view.clicked.connect(self.load)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.view.setText(_translate("MainWindow", "LOAD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

