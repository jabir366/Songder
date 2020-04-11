#!/usr/bin/python3
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import urllib3
import re

http = urllib3.PoolManager()

#html_page = urllib3.urlopen("https://www.masstamilandownload.com/tamil/")
url="https://www.masstamilandownload.com/tamil"
response = http.request('GET', url)
soup = BeautifulSoup(response.data,features="html.parser")
links = []

for link in soup.findAll('a', attrs={'href': re.compile("")}):
    links.append(link.get('href'))

print(links)
