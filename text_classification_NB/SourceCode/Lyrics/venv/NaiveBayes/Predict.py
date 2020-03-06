# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\predict1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import re
from stemming.porter2 import stem
import mysql.connector
class Ui_Predict(object):
    def predct(self, songname):
        my_dict = {}
        stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost',
                     'alone',
                     'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount',
                     'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are',
                     'around',
                     'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before',
                     'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both',
                     'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry',
                     'de',
                     'describe', 'detail', 'did', 'do', 'does', 'doing', 'don', 'done', 'down', 'due', 'during', 'each',
                     'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever',
                     'every',
                     'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill', 'find', 'fire',
                     'first',
                     'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further',
                     'get', 'give', "can't", "won't", "don't",
                     'go', 'had', 'has', 'hasnt', 'have', 'having', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby',
                     'herein',
                     'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', 'ie',
                     'if', 'in', 'inc',
                     'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'just', 'keep', 'last', 'latter',
                     'latterly', 'least',
                     'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more',
                     'moreover', 'most',
                     'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never',
                     'nevertheless', 'next',
                     'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off',
                     'often', 'on',
                     'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves',
                     'out', 'over',
                     'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 's', 'same', 'see', 'seem',
                     'seemed',
                     'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere',
                     'six', 'sixty',
                     'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still',
                     'such',
                     'system', 't', 'take', 'ten', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves',
                     'then', 'thence',
                     'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv',
                     'thin',
                     'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to',
                     'together', 'too', 'top',
                     'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very',
                     'via', 'was',
                     'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter',
                     'whereas',
                     'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who',
                     'whoever', 'whole',
                     'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your',
                     'yours', "''", 'yourself', 'yourselves']
        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='lyrics')
            cursor = database.cursor()
            cursor1 = database.cursor()
            cursor2 = database.cursor()
            cursor.execute("select artist,lyric from dataset where song='" + songname + "'")
            records = cursor.fetchall()
            # print("rec="+str(records))
            for row in records:
                doc = row[1];
                vartist=row[0]
                # print("doc=" +doc)
                c1 = len(doc.split())
                cursor1.execute("select distinct(artist) from dataset");
                fin = 0.0;
                rows = cursor1.fetchall()
                # print("rows=" + str(rows))
                for r in rows:
                    fin = 0.0;
                    print("fin=", fin)
                    artist = r[0]
                    p_c = 0.0
                    res = 0.0
                    print("artist=" + artist)
                    cursor2.execute("select *from dataset where artist='" + artist + "' limit 40 ")
                    rows1 = cursor2.fetchall()

                    for r1 in rows1:
                        # print("rows1=" + str(r1))
                        p_c = 0
                        res = 0
                        docid = r1[0]
                        docn = r1[4]
                        c2 = len(docn.split())
                        # print("docn=" + docn)
                        # print("c2=",c2)
                        p_c = c2 / (c1 + c2)
                        token = re.split(r'[;,\s]\s*', docn)  # docn.split()
                        print("tk=", token)
                        content = str(doc).lower()
                        count = 0
                        # print("cnt="+content)
                        unique_list = []
                        for x in filter(None, token):
                            # check if exists in unique_list or not
                            if x.lower() not in unique_list:
                                unique_list.append(x.lower())

                        for word in unique_list:
                            if (word.lower() not in stopwords):
                                count = count + content.count(word.lower())
                        print(docid + "  " + str(count))
                        tk = int(count) + 1
                        res = float(tk / (c1 + c2 + 1));
                        # print("res=", res)
                        res = float(p_c * res)
                        # print("res1=", res)
                        fin = fin + res
                        print("fin=", fin)
                    print("Summation of " + artist + " " + str(fin))
                    my_dict[artist] = fin
                    print(my_dict)
                key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
                print('Maximum Value: ', my_dict[key_max])
                self.predict.setText(key_max)
                self.actual.setText(vartist)
                if(key_max==vartist):
                    self.status.setText("( Positive )")
                else:
                    self.status.setText("( Negative )")
                self.lyrics.setText(doc)
                self.song.setText(songname)



        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 470)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 21))
        self.label.setStyleSheet("color: rgb(85, 85, 127);\n"
"font: 75 12pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.song = QtWidgets.QLabel(Dialog)
        self.song.setGeometry(QtCore.QRect(130, 50, 121, 21))
        self.song.setStyleSheet("color: rgb(85, 85, 0);\n"
"font: 12pt \"Times New Roman\";")
        self.song.setObjectName("song")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 101, 16))
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);\n"
"font: 75 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.predict = QtWidgets.QLabel(Dialog)
        self.predict.setGeometry(QtCore.QRect(140, 140, 141, 20))
        self.predict.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";")
        self.predict.setObjectName("predict")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 47, 21))
        self.label_3.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.lyrics = QtWidgets.QTextEdit(Dialog)
        self.lyrics.setGeometry(QtCore.QRect(40, 210, 261, 161))
        self.lyrics.setObjectName("lyrics")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 93, 91, 20))
        self.label_4.setStyleSheet("color: rgb(10, 127, 123);\n"
"font: 75 12pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.actual = QtWidgets.QLabel(Dialog)
        self.actual.setGeometry(QtCore.QRect(130, 93, 91, 20))
        self.actual.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 12pt \"Times New Roman\";")
        self.actual.setObjectName("actual")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(230, 140, 81, 21))
        self.status.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";")
        self.status.setObjectName("status")
        '''self.graph = QtWidgets.QPushButton(Dialog)
        self.graph.setGeometry(QtCore.QRect(120, 390, 75, 23))
        self.graph.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Times New Roman\";")
        self.graph.setObjectName("graph")'''

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Predict Performer"))
        self.label.setText(_translate("Dialog", "Song Name :"))
        self.song.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "Predict Artist :"))
        self.predict.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "Lyrics"))
        self.label_4.setText(_translate("Dialog", "Actual Artist :"))
        self.actual.setText(_translate("Dialog", "TextLabel"))
        self.status.setText(_translate("Dialog", "TextLabel"))
        #self.graph.setText(_translate("Dialog", "GRAPH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Predict()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

