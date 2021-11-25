import requests
from bs4 import BeautifulSoup
import datetime
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='python',
                           db='python', charset='utf8', port=3305)
     
curs = conn.cursor()

now = datetime.datetime.now()
in_time = now.strftime("%Y%m%d. %H%M")

response = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
response.encoding = 'euc-kr'

html = response.text
soup = BeautifulSoup(html, 'html.parser')

# print(soup)

st2s = soup.select(".st2")

for idx, st2 in enumerate(st2s):
    s_name = st2.text
    s_code = st2.select("a")[0].attrs['title']
    price = st2.parent.select("td")[1].text.replace(",", "")
    print(s_name, s_code, price)
    
    # print(st2.parent.select("td")[1].text.replace(",", ""))
    # a = st2.select("a")
    # print(a[0].attrs['title'])
    
    val = (s_code, s_name, price, in_time)
    sql = "INSERT INTO stock (s_code, s_name, price, in_time) VALUES (%s,%s,%s,%s)"
    cnt = curs.execute(sql, val)
    print("cnt", cnt)
    conn.commit()

curs.close()
conn.close()
end = datetime.datetime.now()
print(end - now)
