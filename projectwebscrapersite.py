import html5lib
import requests
from bs4 import BeautifulSoup
data="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
res=requests.get(data)
soup=BeautifulSoup(res.content,'html5lib')
price=soup.find_all('h4',class_='price float-end card-title pull-right')
pric=[]
for i in price:
                   name=i.text
                   pric.append(name)

title=soup.find_all('a',{'class':'title'})
titl=[]
for i in title:
                    name=i.text
                    titl.append(name)

titl

description=[]
des=soup.find_all('p',{'class':'description card-text'})
descp=[]
for i in des:
                      name=i.text
                      descp.append(name)

rate=soup.find_all('p',attrs={'data-rating':True})
ratings = [elem.get('data-rating') for elem in rate]

reviews=soup.find_all('p',{'class':'review-count float-end'})
review=[]
for i in reviews:
                         name=i.text
                         review.append(name)

import pandas as pd
table=pd.DataFrame({"price":pric,"name":titl,"description":descp,"rating":ratings,"reviews":review})
z=table.to_csv('D:\cardatawebscraping.csv')
z

