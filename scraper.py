import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.alko.fi/INTERSHOP/web/WFS/Alko-OnlineShop-Site/fi_FI/-/EUR/ViewProduct-Include?SKU=319027&amp;AppendStoreList=true&amp;AjaxRequestMarker=true#'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
stores = page_soup.findAll("span",{"class":"store-in-stock"})
values = page_soup.findAll("span",{"class":"right"})

filename = "gambiinat.txt"
f = open(filename,"w")
headers = "FINLAND'S GAMBINA SITUATION \n"
f.write(headers)

for i in range(0,334):
    singleStore = stores[i].text
    singleValue = values[i+1].text
    print(singleStore+" "+singleValue)
    f.write(singleStore+" "+singleValue+"\n")


