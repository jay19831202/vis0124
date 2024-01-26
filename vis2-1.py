# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:32:48 2024

@author: jay19
"""
import csv
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

fn="result.csv"
csvfile=open(fn,'w',encoding='utf-8')
    
f=csv.writer(csvfile)


urlname='file:./stock.html'

html=urlopen(urlname)

bsobj=BeautifulSoup(html,'lxml')

cnt=0