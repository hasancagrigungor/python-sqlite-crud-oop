import sqlite3
import pandas as pd

class Database:
    
    def __init__(self,db_name):
        self.conn=sqlite3.connect(db_name)
        self.c=self.conn.cursor()

    def yenitablo(self,tabloisim,*sutunlar):
        sutunlar=str(sutunlar)
        sutunlar=sutunlar.replace("'","")
        sutunlar=sutunlar.replace('"',"")
        sql=f"CREATE TABLE IF NOT EXISTS {tabloisim}{sutunlar}"
        self.c.execute(sql)
        self.conn.commit()
    
    def ekle(self,tabloisim,*veriler):
        placeholder=",".join(len(veriler)*["?"])
        sql=f"INSERT INTO {tabloisim} VALUES({placeholder})"
        self.c.execute(sql,veriler)
        self.conn.commit()
    
    def getir(self,tabloisim,where=None):
        sql=f"SELECT * FROM {tabloisim}"
        if where:
            sql=sql+f' WHERE {where}'
        self.c.execute(sql)
        return self.c.fetchall()
    
    def duzenle(self,tabloisim,set,where):
        sql=f"UPDATE {tabloisim} SET {set} WHERE {where}"
        self.c.execute(sql)
        self.conn.commit()

    def sil(self,tabloisim,where):
        sql=f"DELETE FROM {tabloisim} WHERE {where}"
        self.c.execute(sql)
        self.conn.commit()

    def excelcikti(self,tabloisim):
        sql=f"SELECT * FROM {tabloisim}"
        self.c.execute(sql)
        veri=self.c.fetchall()
        sutunlar=[]
        isimler=self.c.description
        for i in isimler:
            sutunlar.append(i[0])
        df=pd.DataFrame(veri,columns=sutunlar)
        df.to_excel(tabloisim+'.xlsx')
    def varmi(self,tabloisim,where):
        sql=f"SELECT * FROM {tabloisim} WHERE {where}"
        self.c.execute(sql)
        veri=self.c.fetchall()
        if len(veri)>0:
            return True
        else:
            return False
    
    def cikis(self):
        self.conn.close()
