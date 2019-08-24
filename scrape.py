#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:41:31 2019

@author: cheungjoey
"""

from bs4 import BeautifulSoup
import pandas as pd
import re

infile = open("filename.txt","r")

contents = infile.read()

soup = BeautifulSoup(contents,'xml') #Adjust file type here

tag = '' #Put html tag to search for here
titles = soup.find_all(tag)

values = []
substring = "" #Checks the string for this substring if necessary
remove = '' #Part of text to remove with regex
for title in titles:
    if substring in title.get_text():
        extracted = re.sub(remove, '', title.get_text())
        values.append(extracted)
        print(extracted)

df = pd.DataFrame({'key': values})

df.to_csv('output.csv', encoding='utf-8', index=False, header=None)
