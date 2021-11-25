import pymysql

class DaoStudent:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8',port=3305)
        
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def select(self):
 
        sql = "select s_id, s_name, s_ban, s_bunho from student"
        self.curs.execute(sql)
 
        rows = self.curs.fetchall()
        return rows   
       
    def insert(self, s_id, s_name, s_ban, s_bunho): 
        sql = f"""
            INSERT INTO student
                (s_id, s_name, s_ban, s_bunho) 
            VALUES 
                ({s_id}, '{s_name}', {s_ban}, {s_bunho})
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()   
        return cnt
        
        
    def update(self, s_id, s_name, s_ban, s_bunho):
        sql = f"""
            update student
            set 
            s_name={s_name},
            s_ban={s_ban},
            s_bunho={s_bunho}
            where
            s_id={s_id}
        """
        cnt = self.curs.execute(sql)
        self.conn.commit() 
        return cnt
    
    def delete(self,s_id):
        sql = f"""
            delete from student
            where
            s_id={s_id}
        """
        cnt = self.curs.execute(sql)
        self.conn.commit() 
        return cnt
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    ds = DaoStudent()
    
    rows = ds.select()
    print(rows)
   
    # cnt = ds.insert("2", "2", "2", "2")    
    # print("cnt",cnt)
    
    # cnt = ds.update("1", "3", "3", "3")    
    # print("cnt",cnt)
    
    # cnt = ds.delete("2")    
    # print("cnt",cnt)
        