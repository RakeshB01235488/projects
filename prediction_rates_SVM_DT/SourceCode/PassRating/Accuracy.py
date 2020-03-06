
from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.tree import DecisionTreeClassifier# DecisionTree Classifier model
import pandas as pd
import numpy as np
from Barchart import view
from sklearn import svm # Support Vector Machine Classifier model
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
class Accuracy_SVM_DT(object):

    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName)
        self.lineEdit.setText(fileName)

    def browse_file1(self):
        fileName1, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName1)
        self.lineEdit_2.setText(fileName1)

    def acuracy(self):
        try:
            training_dataset = self.lineEdit.text()
            testing_dataset = self.lineEdit_2.text()
            if training_dataset == "" or training_dataset == "null" or testing_dataset == "" or testing_dataset == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                df = pd.read_csv(training_dataset, sep=";")
                df1 = pd.read_csv(testing_dataset, sep=";")

                print("\nStudent Performance Prediction")

                # Training Dataset
                # For each feature, encode to categorical values
                class_le = LabelEncoder()
                for column in df[
                    ["school", "sex", "address", "famsize", "Pstatus", "Mjob", "Fjob", "reason", "guardian",
                     "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic"]].columns:
                    df[column] = class_le.fit_transform(df[column].values)


                # Encode G1, G2, G3 as pass or fail binary values
                for i, row in df.iterrows():
                    if row["G1"] >= 10:
                        df["G1"][i] = 1
                    else:
                        df["G1"][i] = 0

                    if row["G2"] >= 10:
                        df["G2"][i] = 1
                    else:
                        df["G2"][i] = 0

                    if row["G3"] >= 10:
                        df["G3"][i] = 1
                    else:
                        df["G3"][i] = 0

                # Target values are G3
                y = df.pop("G3")
                # print("Y=",y)
                # Feature set is remaining features
                X = df


                # Testing Dataset

                for column in df1[
                    ["school", "sex", "address", "famsize", "Pstatus", "Mjob", "Fjob", "reason", "guardian",
                     "schoolsup", "famsup",
                     "paid", "activities", "nursery", "higher", "internet", "romantic"]].columns:
                    df1[column] = class_le.fit_transform(df1[column].values)

                # Encode G1, G2, G3 as pass or fail binary values
                for i, row in df1.iterrows():
                    if row["G1"] >= 10:
                        df1["G1"][i] = 1
                    else:
                        df1["G1"][i] = 0

                    if row["G2"] >= 10:
                        df1["G2"][i] = 1
                    else:
                        df1["G2"][i] = 0

                    if row["G3"] >= 10:
                        df1["G3"][i] = 1
                    else:
                        df1["G3"][i] = 0

                        # Target values are G3
                y1 = df1.pop("G3")

                # Feature set is remaining features
                X1 = df1
                param_grid = {'max_depth': np.arange(3, 10)}
                clf_dt = DecisionTreeClassifier()
                gs_dt = GridSearchCV(clf_dt, param_grid,cv=10)
                gs_dt.fit(X, y)
                predicted_class = gs_dt.predict(X1)
                accuracy_dt = self.getAccuracy(y1, predicted_class)
                print("ac_dt", accuracy_dt)



                parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 10]}
                clf_svm = svm.SVC()
                gs_svm = GridSearchCV(clf_svm,parameters,cv=10)
                gs_svm.fit(X, y)
                predicted_class1 = gs_svm.predict(X1)
                accuracy_svm= self.getAccuracy(y1, predicted_class1)
                print("ac_svm", accuracy_svm)


                #Barchart
                list = []
                list.clear()
                list.append(accuracy_svm)
                list.append(accuracy_dt)
                view(list)






        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def getAccuracy(self,testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
            print("actual=", testSet[x])
            print("predict=", predictions[x])
            if testSet[x] == predictions[x]:
                correct += 1
        return (correct / float(len(testSet))) * 100.0

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(712, 535)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 60, 421, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Georgia\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 150, 191, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 200, 341, 41))
        self.lineEdit.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 200, 121, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 420, 131, 41))
        self.pushButton_2.setStyleSheet("font: 14pt \"Georgia\";\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.acuracy)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 280, 221, 51))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 340, 341, 41))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 340, 121, 41))
        self.pushButton_3.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.browse_file1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Student Pass Rating Prediction"))
        self.label.setText(_translate("Dialog", "Performance Results"))
        self.label_2.setText(_translate("Dialog", "Load Training Dataset"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "GetAccuracy"))
        self.label_3.setText(_translate("Dialog", "Load Testing Dataset"))
        self.pushButton_3.setText(_translate("Dialog", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    sys.exit(app.exec_())

