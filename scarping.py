import requests
from bs4 import BeautifulSoup

urls = [ "https://www.ufc.com/athletes/all?gender=All&search=&page={0}".format(i) for i in range(2,20) ]

file = open('joueur.txt','w',encoding='utf-8')

for url in urls :
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    print(url)
    for link in soup.find_all('div', attrs={"class":"c-listing-athlete-flipcard__front"}):
        file.write("{0}\n".format(link.text))