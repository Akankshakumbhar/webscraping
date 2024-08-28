### application
fectching data from
1)social media
2)machine learning data
3)hotel data



import requests
import html5lib
from bs4 import BeautifulSoup
data ="https://webscraper.io/test-sites"
res=requests.get(data)
print(res.content)
soup=BeautifulSoup(res.content,'html5lib')
print(soup.prettify())

## tags
tags=soup.header.a
tags
tags=soup.header.a
tags
'''<a data-bs-target=".side-collapse" data-bs-target-2=".side-collapse-container" data-bs-toggle="collapse-side">
                                <button aria-controls="navbar" aria-expanded="false" class="navbar-toggler float-end collapsed" data-bs-target="#navbar" data-bs-target-2=".side-collapse-container" data-bs-target-3=".side-collapse" data-bs-toggle="collapse" type="button">

                                        <span class="visually-hidden">Toggle navigation</span>
                                        <span class="icon-bar top-bar"></span>
                                        <span class="icon-bar middle-bar"></span>
                                        <span class="icon-bar bottom-bar"></span>
                                        <span class="icon-bar extra-bottom-bar"></span>

                                </button>
                        </a>
'''
# attributes
#tags=soup.header.a
##tags.attrs

 #find all

soup.find('header')
#output:header relatedwill
soup.find('div',{'class':'container-fluid blog-hero'}) # sepecfic class we need tofind
#output::
'''
<div class="container-fluid blog-hero">
                <div class="container">
                        <div class="row">
                                <div class="col-lg-12">
                                        <h1>Test Sites</h1>
                                </div>
                        </div>
                </div>
        </div>
'''
soup.find('p',{'class':'pull-right-price'})



###### find all(function)
soup.find_all('p')
'''
[<p>Web Scraper</p>, <p>Cloud Scraper</p>, <p>Pricing</p>, <p>Learn</p>, <p style="font-size:21px;">
                        Here are some sites that you can use for training while learning how to
                        use the Web Scraper.
                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        All items are loaded in one page.
                                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Standard links are used for pagination.
                                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Dynamic links that use data without reloading the page for
                                        pagination.
                                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Instead of using pagination this site uses a "Load more"
                                        button to load more items.
                                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Instead of using pagination this site loads items when user
                                        scrolls the page down.
                                </p>, <p class="lead">
                                        This page contains multiple tables. You can train using Table
                                        selector here.
                                </p>, <p>Products</p>, <p>Company</p>, <p>Resources</p>, <p>CONTACT US</p>, <p class="copyright">Copyright © 2024
                                        <b>Web Scraper</
'''
soup.find_all('h4',{'class':'pull-right-price'})[6:]# 6th element
soup.find_all('div',{'class':'wrapper'})
'''
[<div class="wrapper">
                <div class="formenu-here container-fluid">

        </div>
        <div class="container-fluid blog-hero">
                <div class="container">
                        <div class="row">
                                <div class="col-lg-12">
                                        <h1>Test Sites</h1>
                                </div>
                        </div>
                </div>
        </div>


        <div class="container test-sites">
                <p style="font-size:21px;">
                        Here are some sites that you can use for training while learning how to
                        use the Web Scraper.
                </p>

                <hr class="test-site-divider"/>

                <div class="row test-site">
                        <div class="col-lg-7 order-lg-2">
                                <h2 class="site-heading">
                                        <a href="/test-sites/e-commerce/allinone">
                                                E-commerce site
                                        </a>
                                </h2>
                                <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        All items are loaded in one page.
                                </p>
                        </div>
                        <div class="col-lg-5 order-lg-1">
                                <img alt="E-commerce site" src="/images/test-sites/screens/test-sites-ecommerce-allinone.png"/>
                        </div>
                </div>
                <hr class="test-site-divider"/>

                <div class="row test-site">
                        <div class="col-lg-7 order-lg-2">
                                <h2 class="site-heading">
                                        <a href="/test-sites/e-commerce/static">
                                                E-commerce site with pagination links
                                        </a>
                                </h2>
                                <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Standard links are used for pagination.
                                </p>
                        </div>
                        <div class="col-lg-5 order-lg-1">
                                <img alt="E-commerce site" src="/images/test-sites/screens/test-sites-ecommerce-static.png"/>
                        </div>
                </div>
                <hr class="test-site-divider"/>

                <div class="row test-site">
                        <div class="col-lg-7 order-lg-2">
                                <h2 class="site-heading">
                                        <a href="/test-sites/e-commerce/ajax">
                                                E-commerce site with AJAX pagination links
                                        </a>
                                </h2>
                                <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Dynamic links that use data without reloading the page for
                                        pagination.
                                </p>
                        </div>
                        <div class="col-lg-5 order-lg-1">
                                <img alt="E-commerce site" src="/images/test-sites/screens/test-sites-ecommerce-ajax.png"/>
                        </div>
                </div>
                <hr class="test-site-divider"/>

                <div class="row test-site">
                        <div class="col-lg-7 order-lg-2">
                                <h2 class="site-heading">
                                        <a href="/test-sites/e-commerce/more">
                                                E-commerce site with "Load more" buttons
                                        </a>
                                </h2>
                                <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Instead of using pagination this site uses a "Load more"
                                        button to load more items.
                                </p>
                        </div>
                        <div class="col-lg-5 order-lg-1">
                                <img alt="E-commerce site" src="/images/test-sites/screens/test-sites-ecommerce-more.png"/>
                        </div>
                </div>
                <hr class="test-site-divider"/>

                <div class="row test-site">
                        <div class="col-lg-7 order-lg-2">
                                <h2 class="site-heading">
                                        <a href="/test-sites/e-commerce/scroll">
                                                E-commerce site that loads items while scrolling
                                        </a>
                                </h2>
                                <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Instead of using pagination this site loads items when user
                                        scrolls the page down.
                                </p>
                        </div>
                        <div class="col-lg-5 order-lg-1">
                                <img alt="E-commerce site" src="/images/test-sites/screens/test-sites-ecommerce-allinone.png"/>
                        </div>
                </div>
                <hr class="test-site-divider"/>

                <div class="row test-site">
                        <div class="col-lg-7 order-lg-2">
                                <h2 class="site-heading">
                                        <a href="/test-sites/tables">Table playground
                                        </a>
                                </h2>
                                <p class="lead">
                                        This page contains multiple tables. You can train using Table
                                        selector here.
                                </p>
                        </div>
                        <div class="col-lg-5 order-lg-1">
                                <img alt="table playground" src="/images/test-sites/screens/test-sites-tables.png"/>
                        </div>
                </div>

        </div>
        <div class="clearfix"></div>
        <div class="push"></div>
</div>]'''



soup.find_all(['h4','p'])
'''[<p>Web Scraper</p>, <p>Cloud Scraper</p>, <p>Pricing</p>, <p>Learn</p>, <p style="font-size:21px;">
                        Here are some sites that you can use for training while learning how to
                        use the Web Scraper.
                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        All items are loaded in one page.
                                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Standard links are used for pagination.
                                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Dynamic links that use data without reloading the page for
                                        pagination.
                                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Instead of using pagination this site uses a "Load more"
                                        button to load more items.
                                </p>, <p class="lead">
                                        E-commerce site with multiple categories, subcategories.
                                        Instead of using pagination this site loads items when user
                                        scrolls the page down.
                                </p>, <p class="lead">
                                        This page contains multiple tables. You can train using Table
                                        selector here.
                                </p>, <p>Products</p>, <p>Company</p>, <p>Resources</p>, <p>CONTACT US</p>, <p class="copyright">Copyright © 2024
                                        <b>Web Scraper</b> | All rights reserved</p>]
'''

soup.find_all(['h4','p','a']) ## <p>and <a>tag asthe output



soup.find_all(id=True)
'''
[<header class="navbar fixed-top navbar-expand-lg navbar-dark navbar-static svg-background" id="navbar-top" role="banner">
        <div class="container">

                <div class="navbar-header">

                        <a data-bs-target=".side-collapse" data-bs-target-2=".side-collapse-container" data-bs-toggle="collapse-side">
                                <button aria-controls="navbar" aria-expanded="false" class="navbar-toggler float-end collapsed" data-bs-target="#navbar" data-bs-target-2=".side-collapse-container" data-bs-target-3=".side-collapse" data-bs-toggle="collapse" type="button">

                                        <span class="visually-hidden">Toggle navigation</span>
                                        <span class="icon-bar top-bar"></span>
                                        <span class="icon-bar middle-bar"></span>
                                        <span class="icon-bar bottom-bar"></span>
                                        <span class="icon-bar extra-bottom-bar"></span>

                                </button>
                        </a>
                        <div class="navbar-brand">
                                <a href="/"><img alt="Web Scraper" src="/img/logo_white.svg"/></a>
                        </div>
                </div>

                <div class="side-collapse in">
                        <nav class="navbar-collapse collapse" id="navbar" role="navigation">
                                <ul class="nav navbar-nav navbar-right">
                                        <li class="nav-item">
                                                <a class="nav-link menuitm" href="/">
                                                        <p>Web Scraper</p>
                                                        <div class="crta"></div>
                                                </a>
                                        </li>
                                        <li class="nav-item">
                                                <a class="nav-link menuitm" href="/cloud-scraper" id="cloud-nav-link">
                                                        <p>Cloud Scraper</p>
                                                        <div class="crta"></div>
                                                </a>
                                        </li>
                                        <li class="nav-item">
                                                <a class="nav-link menuitm" href="/pricing" id="pricing-nav-link">
                                                        <p>Pricing</p>
                                                        <div class="crta"></div>
                                                </a>
                                        </li>
                                        <li class="nav-item dropdown">
                                                <button aria-expanded="false" aria-haspopup="true" class="menuitm nav-link dropdown-toggle" data-bs-toggle="dropdown" id="dropdownMenuLink" role="button">'''

import re
soup.find_all(string=re.compile('Nok'))
## if wewant the sepechic code for nokia phone we  can find with with the help of regular expression

soup.find_all('p',class_=re.compile('pull'),limit=3) #pullis the class same and we want oly 3 lement from pull element
soup.find_all('h4',{'class':'price float-end card-title pull-right'})
'''[<h4 class="price float-end card-title pull-right">$899.99</h4>, <h4 class="price float-end card-title pull-right">$93.99</h4>, <h4 class="price float-end card-title pull-right">$499.99</h4>]'''

soup.find_all('a',{'class':'title'})
#a class="title" href="/test-sites/e-commerce/allinone/product/8" title="Iphone">Iphone</a>, <a class="title" href="/test-sites/e-commerce/allinone/product/3" title="Samsung Galaxy">Samsung Galaxy</a>, <a class="title" href="/test-sites/e-commerce/allinone/product/6" title="Ubuntu Edge">Ubuntu Edge</a>]

price=soup.find_all('h4')
price
'''<h4 class="price float-end card-title pull-right">$899.99</h4>, <h4>
                                        <a class="title" href="/test-sites/e-commerce/allinone/product/8" title="Iphone">Iphone</a>
                                </h4>, <h4 class="price float-end card-title pull-right">$93.99</h4>, <h4>
                                        <a class="title" href="/test-sites/e-commerce/allinone/product/3" title="Samsung Galaxy">Samsung Galaxy</a>
                                </h4>, <h4 class="price float-end card-title pull-right">$499.99</h4>, <h4>
                                        <a class="title" href="/test-sites/e-commerce/allinone/product/6" title="Ubuntu Edge">Ubuntu Edge</a>
                                </h4>]
'''
# reviews

reviews=soup.find_all('p',{'class':'review-count float-end'})
'''
to find reviews from the website

>>> reviews
[<p class= 
'''

#description

'''
description=soup.find_all('p',{'class':'description card-text'})
description
[<p class="description card-text">Silver</p>, <p class="description card-text">5 mpx. Android 5.0</p>, <p class="description card-text">Sapphire glass</p>]
>>>
'''


# if we want onlt text eg rating i nat only 8 or 7 in hat case(find is used_)
#reviews=soup.find('p',{'class':'review-count float-end'}).text
#reviews
'8 reviews'


# want all elemnet from the review
o=[]
for i in reviews:
    name=i.text
    o.append(name)


print(o)

## for price
'''
price=soup.find_all('h4',{'class':'price float-end card-title pull-right'})
>>> price
[<h4 class="price float-end card-title pull-right">$899.99</h4>, <h4 class="price float-end card-title pull-right">$93.99</h4>, <h4 class="price float-end card-title pull-right">$499.99</h4>]
>>> t=[]
>>> for i in price:
...                      price=i.text
...                      t.append(price)
...
>>> t(output)

['$899.99', '$93.99', '$499.99']
'''

# converting all columnssuch asprice,rating etc into dataframes


reviews=soup.find_all('p',{'class':'review-count float-end'})
''''>>> reviews
[<p class="review-count float-end">8 reviews</p>, <p class="review-count float-end">3 reviews</p>, <p class="review-count float-end">2 reviews</p>]
>>> y=[]
>>> for i in reviews:
...                      rev=i.text
...                      y.append(rev)
...
>>> y
['8 reviews', '3 reviews', '2 reviews']
'''


 #converting all into dataframe

import pandas as pd

table=pd.DataFrame({'price':t,'reviews':y})
table
     '''price    reviews
0  $899.99  8 reviews
1   $93.99  3 reviews
2  $499.99  2 reviews
'''
#writing the data into csv or excel
# give the path
table.to_csv('path of new csv file')


 # particular class or contanier
boxes=soup.find_all('div',{'class':'col-md-4 col-xl-4 col-lg-4'})[1]# 1 means limit 1
boxes
boxes.find('a').text
'Samsung Galaxy'
boxes.find('p').text
'5 mpx. Android 5.0'
boxes.find('p').text


### this is for 2nd container [2]
boxes=soup.find_all('div',{'class':'col-md-4 col-xl-4 col-lg-4'})[2]
boxes
'''<div class="col-md-4 col-xl-4 col-lg-4">
        <div class="card thumbnail">
                <div class="product-wrapper card-body">
                        <img alt="item" class="img-fluid card-img-top image img-responsive" src="/images/test-sites/e-commerce/items/cart2.png"/>
                        <div class="caption">
                                <h4 class="price float-end card-title pull-right">$499.99</h4>
                                <h4>
                                        <a class="title" href="/test-sites/e-commerce/allinone/product/6" title="Ubuntu Edge">Ubuntu Edge</a>
                                </h4>
                                <p class="description card-text">Sapphire glass</p>

                        </div>
                        <div class="ratings">
                                <p class="review-count float-end">2 reviews</p>
                                <p data-rating="1">
                                                                                <span class="ws-icon ws-icon-star"></span>
                                                                        </p>
                        </div>
                </div>
        </div>
</div>
>>> boxes.find('a').text
'Ubuntu Edge'
>>> boxes.find('p').text
'Sapphire glass'
'''