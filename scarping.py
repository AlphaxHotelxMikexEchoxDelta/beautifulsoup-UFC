import requests
from bs4 import BeautifulSoup
import re

file = open('joueur.txt','w',encoding='utf-8')
URL = "https://www.ufc.com/rankings"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

###########################################################
listu = []
for link in soup.find_all('div', attrs={"class":"info"}):
    listu.append(link.text)

listo = [ i for i in listu[:-5] ]
listi = [ i for i in listo[1:] ]
lista = [ i.replace('\n',' ') for i in listi ]

file = open('joueur.txt','w',encoding='utf-8')

for i in lista:
    file.write( i+"\n" )

#############################################################

for link in soup.find_all("a"):
    print(link.get("href"))