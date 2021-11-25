import pymysql
 
def getPrices(s_name):
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='python',
                           db='python', charset='utf8', port=3305)
    curs = conn.cursor()
    
     
    sql = "select price from stock where s_name='{}'".format(s_name)
    curs.execute(sql)
    
    rows = curs.fetchall()  
    for row in rows :
        ret.append(row[0])
    conn.close()
    return ret 

if __name__ == '__main__':
    arr = getPrices('삼성전자')
    print(arr)