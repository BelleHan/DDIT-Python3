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
 
 
def getAllSName():
    ret = []
    conn = pymysql.connect(host='localhost', user='root', password='python',
                           db='python', charset='utf8', port=3305)
    curs = conn.cursor()
    
     
    sql = "SELECT s_name FROM stock GROUP BY s_name"
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

allnames = getAllSName()
print(allnames)

for n in allnames :
    zs.append(getPrices(n))

for idx,n in enumerate(allnames):
    graph.plot(x+idx,y,zs[idx])
    

plt.show()
