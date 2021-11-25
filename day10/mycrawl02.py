import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/emp"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.select("table")
    trs = tables[0].select("tr")
    for idx,tr in enumerate(trs):
        if idx>0:
            # print(idx,tr)
            tds = tr.select("td")
            print(tds[1].text,tds[2].text)

else : 
    print(response.status_code)