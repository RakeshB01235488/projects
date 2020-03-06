from PyQt5 import QtCore, QtGui, QtWidgets
from Predict_SVM import PredictSVM
from Predict_DT import PredictDT
from Accuracy import Accuracy_SVM_DT
class Ui_AdminHome(object):

    def predictsvm(self):

        self.svm = QtWidgets.QDialog()
        self.ui =PredictSVM()
        self.ui.setupUi(self.svm)
        self.svm.show()

    def predictdt(self):

        self.dt = QtWidgets.QDialog()
        self.ui =PredictDT()
        self.ui.setupUi(self.dt)
        self.dt.show()
    def acuracy(self):
        self.acry = QtWidgets.QDialog()
        self.ui = Accuracy_SVM_DT()
        self.ui.setupUi(self.acry)
        self.acry.show()




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 380)
        Dialog.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 80, 231, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predictsvm)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 150, 231, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.predictdt)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 220, 231, 41))
        self.pushButton_3.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.acuracy)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.pushButton.setText(_translate("Dialog", "Support Vector Machine"))
        self.pushButton_2.setText(_translate("Dialog", "Decision Tree"))
        self.pushButton_3.setText(_translate("Dialog", "Performance Results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

