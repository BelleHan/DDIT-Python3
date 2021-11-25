import pymysql
 

conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8', port=3305)
 
curs = conn.cursor()
 
sql = "select * from emp"
curs.execute(sql)

rows = curs.fetchall()
print(rows)     

conn.close()