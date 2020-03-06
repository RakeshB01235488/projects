# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\SongDetails.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from Classification import Ui_Classify
class Ui_SongDetails(object):
    def classify(self):
        lyrics=self.lyrics.toPlainText()
        songnm = self.song.text()
        self.sd = QtWidgets.QDialog()
        self.ui =Ui_Classify()
        self.ui.setupUi(self.sd)
        self.ui.recomanded(lyrics,songnm)
        self.sd.show()
        ##print(lyrics)
        #print(songnm)

    def details(self,song):
        self.song.setText(song)
        database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='lyrics')
        cursor = database.cursor()
        cursor.execute("select artist,lyric from dataset where song='" + song + "'")
        records = cursor.fetchall()
        for row in records:
            self.artist.setText(row[0]);
            self.lyrics.setPlainText(row[1])

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(559, 343)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 101, 21))
        self.label.setStyleSheet("color: rgb(170, 85, 0);\n"
"font: 75 12pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.song = QtWidgets.QLabel(Dialog)
        self.song.setGeometry(QtCore.QRect(130, 60, 151, 21))
        self.song.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";")
        self.song.setObjectName("song")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label_3.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.artist = QtWidgets.QLabel(Dialog)
        self.artist.setGeometry(QtCore.QRect(126, 90, 91, 21))
        self.artist.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";")
        self.artist.setObjectName("artist")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 47, 41))
        self.label_2.setStyleSheet("color: rgb(85, 85, 0);\n"
"font: 75 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.lyrics = QtWidgets.QPlainTextEdit(Dialog)
        self.lyrics.setGeometry(QtCore.QRect(30, 140, 431, 71))
        self.lyrics.setObjectName("lyrics")
        self.predict = QtWidgets.QPushButton(Dialog)
        self.predict.setGeometry(QtCore.QRect(60, 230, 121, 23))
        self.predict.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"font: 75 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.predict.setObjectName("predict")
        self.predict.clicked.connect(self.classify)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Song Details"))
        self.label.setText(_translate("Dialog", "Song Name :"))
        self.song.setText(_translate("Dialog", "song"))
        self.label_3.setText(_translate("Dialog", "Artist Name :"))
        self.artist.setText(_translate("Dialog", "artist"))
        self.label_2.setText(_translate("Dialog", "Lyrics"))
        self.predict.setText(_translate("Dialog", "Classifications"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SongDetails()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

