import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8', port=3305)
 
curs = conn.cursor()
sql = """insert into emp(e_id, name,tel)
         values (%s, %s, %s)"""
curs.execute(sql, (3, '3','3'))
conn.commit()
 
conn.close()