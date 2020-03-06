# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\Classification.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import string
import re
import sys, traceback
import mysql.connector
class Ui_Classify(object):
    def recomanded(self, lyrics, songnm):
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
                     'whoever', 'whole','whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your',
                     'yours', "''", 'yourself', 'yourselves']
        try:
         # print("ly="+lyrics)
          print(songnm)
          database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='lyrics')
          cursor = database.cursor()
          cursor.execute("delete from temp")
          database.commit()
          cursor.execute("select *from dataset where song!='"+songnm+"'")
          records = cursor.fetchall()
          docly=re.split(r'[;,\s]\s*', lyrics)
          c1=str(len(docly))
         # print("docly="+docly)
          print("lenth=" +c1)
          for row in records:
              doc=row[0]
              artist=row[1]
              song=row[2]
              link=row[3]
              lyric=row[4]
              docn=re.split(r'[;,\s]\s*', lyric)
              c2 = str(len(docn))
              p_c=str(int(c2)/int(c1+c2))

              token = re.split(r'[;,\s]\s*', lyric)
              print("tokn=",token)
              content = str(lyrics).lower()
              count = 0
              unique_list = []
              for x in filter(None, token):
                  # check if exists in unique_list or not
                  if x.lower() not in unique_list:
                      unique_list.append(x.lower())
              for word in unique_list:
                  print(" wrd= "+word)
                  if (word.lower() not in stopwords):
                   count = count + content.count(word.lower())

              tk = int(count) + 1
              print("tk=", tk)
              cls = int(c1) + int(c2) + 1
              res = tk / cls
              result = float(p_c) * res
              #print("res=", result)
              #print("doc=" + doc)
              query = "insert into temp values(%s,%s,%s,%s,%s,%s)"
              values = (doc, artist, song, "https://www.lyricsfreak.com"+link, lyric,result)
              cursor.execute(query, values)
              database.commit()
          cursor.execute("SELECT *FROM temp ORDER BY res DESC LIMIT 0,10")
          row = cursor.fetchall()
          self.tableWidget.setRowCount(0)
          for row_number, row_data in enumerate(row):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))






        except Exception as e:
               print("Error="+e.args[0])
               tb = sys.exc_info()[2]
               print(tb.tb_lineno)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 242)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 1, 421, 241))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Songs Recommendations"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Doc"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Artist"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Song Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Link"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Lyric"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Classify()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

