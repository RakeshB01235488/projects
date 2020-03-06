import xlrd
import mysql.connector
class XLDB:
    def insert(self,fname):
        book=xlrd.open_workbook(fname)
        sheet=book.sheet_by_index(0)
        database=mysql.connector.connect(host="localhost",user="root",passwd="root",db='lyrics')
        cursor=database.cursor()
        cursor.execute("delete from dataset")
        database.commit()
        query="insert into dataset values(%s,%s,%s,%s,%s)"
        for r in range(0,sheet.nrows):
            doc=sheet.cell(r,0).value
            artist = sheet.cell(r,1).value
            song = sheet.cell(r,2).value
            link=sheet.cell(r,3).value
            lyrics = sheet.cell(r,4).value
            values=(doc,artist,song,link,lyrics)
            cursor.execute(query,values)
            database.commit()
            columns=str(sheet.ncols)
            # rows=str(sheet.nrows)
            print("inserted")

if __name__ == "__main__":
    obj= XLDB()
    obj.insert("E:\Lyrics.xlsx")