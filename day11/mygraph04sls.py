import numpy as np
import matplotlib.pyplot as plt  
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


fig = plt.figure(1) 
graph = fig.add_subplot(111,projection = '3d')

x = np.zeros(10)
y = range(10)
zs = []

zs.append(getPrices('삼성전자'))
zs.append(getPrices('LG'))
zs.append(getPrices('SK'))


graph.plot(x+0,y,zs[0])
graph.plot(x+1,y,zs[1])
graph.plot(x+2,y,zs[2])

plt.show()
