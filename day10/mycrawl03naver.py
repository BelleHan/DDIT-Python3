import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='python',
                           db='python', charset='utf8', port=3305)
     
curs = conn.cursor()

client_id = "3x9wcef3SixADPdA5YWL"
client_secret = "KywJEH8ETA"
encText = urllib.parse.quote("주식")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    text = response_body.decode('utf-8')
    soup = BeautifulSoup(text, 'xml')
    # print(soup)
    
    items = soup.select("item")
    for idx,item in enumerate(items):
        title = item.title.text
        link = item.link.text
        description = item.description.text
        bloggername = item.bloggername.text
        bloggerlink = item.bloggerlink.text
        postdate = item.postdate.text
         
        sql = f"""
        INSERT INTO naver
            (title,link,description,bloggername,bloggerlink,postdate) 
        VALUES 
            ('{title}','{link}','{description}', '{bloggername}','{bloggerlink}','{postdate}')
        """
        cnt = curs.execute(sql)
        print("cnt", cnt)
        conn.commit()   
        

else:
    print("Error Code:" + rescode)

 
curs.close()
conn.close()


