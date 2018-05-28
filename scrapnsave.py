#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:51:23 2018

@author: vinaymac
"""

#import the library used to query a website
from urllib.request import urlopen
import pandas as pd
import re

#specify the url
wiki = "http://vasanthandco.in"
values=[]
x = 'vasanthandco.in'
#Query the website and return the html to the variable 'page'
page = urlopen(wiki)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
result = []
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

all_links=soup.find_all("a")


homeurls = [el["href"] for el in soup.findAll("a", href=re.compile("home"))]
kitchenurls = [el["href"] for el in soup.findAll("a", href=re.compile("kitchen"))]

#print(homeurls)

for url in homeurls:
    i=0
    temp=url.split("/")[-3:]
    if x in temp: 
        temp.remove(x)
    if temp not in values:
        values.append(temp)
        i=i+1

for url in kitchenurls:
    i=0
    temp=url.split("/")[-3:]
    if x in temp: 
        temp.remove(x)
    if temp not in values:
        values.append(temp)
        i=i+1
 
            

    
df = pd.DataFrame(values)
print("***********************************")
print("Printing dataframe")

out = df.to_json(orient='records')
with open('/Users/vinaymac/Official/file_name.txt', 'w') as f:
    f.write(out)







