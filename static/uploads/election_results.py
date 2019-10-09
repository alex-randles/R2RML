import requests
website_url = requests.get('https://en.wikipedia.org/wiki/2019_Irish_local_elections#Results_by_council').text


import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/2019_Irish_local_elections#Results_by_council"

res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all(['th','td'])
    print(data)
    try:
        country = data[0].a.text
        title = data[1].a.text
        name = data[1].a.find_next_sibling().text
    except IndexError:pass
    print("{}|{}|{}".format(country,title,name))