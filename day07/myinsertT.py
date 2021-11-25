import pymysql
 

conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8', port=3305)
 
curs = conn.cursor()
 
val = (5, "5", "5")
sql = "INSERT INTO emp (e_id,name,tel) VALUES (%s, %s, %s)"
cnt = curs.execute(sql,val)
print("cnt", cnt)
conn.commit()   

curs.close()
conn.close()


