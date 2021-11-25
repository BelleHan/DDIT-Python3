import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8',port=3305)
        
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def select(self):
 
        sql = "select e_id,name,tel from emp"
        self.curs.execute(sql)
 
        rows = self.curs.fetchall()
        return rows   
       
    def insert(self,e_id,name,tel): 
        sql = f"""
            INSERT INTO emp 
                (e_id,name,tel) 
            VALUES 
                ({e_id}, '{name}', '{tel}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()   
        return cnt
        
        # val = (e_id, name, tel)
        # sql = "INSERT INTO emp (e_id,name,tel) VALUES (%s, %s, %s)"
        # cnt = self.curs.execute(sql,val)
        # self.conn.commit()   
        # return cnt
        
    def update(self,e_id,name,tel):
        sql = f"""
            update emp
            set 
                name='{name}',
                tel='{tel}'
            where
                e_id={e_id}
        """
        cnt = self.curs.execute(sql)
        self.conn.commit() 
        return cnt
    
    def delete(self,e_id):
        sql = f"""
            delete from emp
            where
                e_id={e_id}
        """
        cnt = self.curs.execute(sql)
        self.conn.commit() 
        return cnt
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    rows = de.select()
    print(rows)
   
    # cnt = de.insert("4", "3", "3")    
    # print("cnt",cnt)
    
    # cnt = de.update("3", "4", "4")    
    # print("cnt",cnt)
    
    # cnt = de.delete("4")    
    # print("cnt",cnt)
        