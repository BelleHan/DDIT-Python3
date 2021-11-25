import pymysql
 

conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8', port=3305)
 
curs = conn.cursor()
 
e_id = "3"
name = "4"
tel = "4"
sql = f"""
update emp
set 
name={name},
tel={tel}
where
e_id={e_id}
"""
cnt = curs.execute(sql)
print("cnt", cnt)
conn.commit()   

curs.close()
conn.close()


