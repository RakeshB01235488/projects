# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from XLDB import XLDB
from SongList import Ui_SongList
from Predict import Ui_Predict
class Ui_Dialog(object):
    def browsefile(self):
        fileName,_ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "E://","*.xlsx")
        print(fileName)
        self.lineEdit.setText(fileName)
    def loadfile(self):
        fnm=self.lineEdit.text()
        obj=XLDB()
        obj.insert(fnm)
        #print("fnm="+fnm)
        self.lineEdit.setText("")
        self.showMessageBox("Information","Dataset Loaded Successfully")
    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def search(self):
        songname=self.lineEdit_2.text()
        print(songname)
        self.song = QtWidgets.QDialog()
        self.ui = Ui_SongList()
        self.ui.setupUi(self.song)
        self.ui.songlist(songname)
        self.song.show()
    def prediction(self):
        songname = self.lineEdit_2.text()
        print(songname)
        self.p = QtWidgets.QDialog()
        self.ui = Ui_Predict()
        self.ui.setupUi(self.p)
        self.ui.predct(songname)
        self.p.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 503)
        self.home = QtWidgets.QTabWidget(Dialog)
        self.home.setGeometry(QtCore.QRect(10, 10, 551, 561))
        self.home.setStyleSheet("")
        self.home.setObjectName("home")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 0, 551, 481))
        self.label.setStyleSheet("background-image: url(E://QT/arch.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.home.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.load = QtWidgets.QPushButton(self.tab_2)
        self.load.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.load.setStyleSheet("background-color: rgb(170, 170, 0);\n"
"font: 8pt \"Times New Roman\";\n"
"font: 75 12pt \"Times New Roman\";")
        self.load.setObjectName("load")
        self.load.clicked.connect(self.loadfile)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(130, 160, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(130, 140, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.browse = QtWidgets.QPushButton(self.tab_2)
        self.browse.setGeometry(QtCore.QRect(420, 162, 81, 31))
        self.browse.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 11pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Times New Roman\";")
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.browsefile)
        self.home.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 140, 311, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 111, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(230, 180, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(85, 0, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)
        self.predict = QtWidgets.QPushButton(self.tab_3)
        self.predict.setGeometry(QtCore.QRect(330, 180, 75, 23))
        self.predict.setStyleSheet("background-color: rgb(170, 85, 0);\n"
                                   "font: 75 11pt \"Times New Roman\";\n"
                                   "color: rgb(255, 255, 255);")
        self.predict.setObjectName("predict")
        self.predict.clicked.connect(self.prediction)
        self.home.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.home.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lyrics Classifications"))
        self.home.setTabText(self.home.indexOf(self.tab), _translate("Dialog", "HOME"))
        self.load.setText(_translate("Dialog", "Load"))
        self.label_2.setText(_translate("Dialog", "File"))
        self.browse.setText(_translate("Dialog", "Browse"))
        self.home.setTabText(self.home.indexOf(self.tab_2), _translate("Dialog", "Load DataSet"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Enter Song Name</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.home.setTabText(self.home.indexOf(self.tab_3), _translate("Dialog", "Search"))
        self.predict.setText(_translate("Dialog", "Predict"))

#import home1_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

