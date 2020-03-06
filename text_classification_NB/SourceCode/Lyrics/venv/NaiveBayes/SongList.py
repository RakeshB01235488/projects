# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\SongList.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SongDetails import Ui_SongDetails
import mysql.connector
class Ui_SongList(object):
    def songlist(self,song):
        database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='lyrics')
        cursor = database.cursor()
        cursor.execute("select song from dataset where song like '%"+song+"%'")
        records = cursor.fetchall()
        for row in records:
           self.listWidget.addItem( row[0]);
    def songDetails(self):
        song=self.listWidget.currentItem().text()
        self.sd = QtWidgets.QDialog()
        self.ui = Ui_SongDetails()
        self.ui.setupUi(self.sd)
        self.ui.details(song)
        self.sd.show()
        print(song)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(343, 313)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.songDetails)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 20))
        self.label.setStyleSheet("color: rgb(85, 85, 0);\n"
"font: 75 10pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SongsList"))
        self.label.setText(_translate("Dialog", " Select Song"))
        #self.view.setText(_translate("Dialog", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SongList()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

