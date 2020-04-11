#!/usr/bin/python3
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import urllib3
import re
import os

def get_urls():
    """
    return list of URLs which has almosts all the songs stored in dirs
    year wise
    """
    urls =[]
    urls.append({"description":"tamil songs","language":"Tamil","url":"https://knewdownload.info"})
    urls.append({"description":"Malayalam songs","language":"Malayalam","url":"https://knewdownload.info/Malayalam"})
    urls.append({"description":"Malayalam songs","language":"Hindi","url":"https://pagaldownload.info/Bollywood"})
    return urls

def get_links(pattern,url=''):
    print("URL is :",url)
    http = urllib3.PoolManager()
    response = http.request('GET', URL+url)
    soup = BeautifulSoup(response.data,features="html.parser")
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile(pattern)}):
        print(link)
        #print(link.get('href').get('contents'))
        link_text =  link.get('href')
        print("link_text:",link_text,"url:",url)
        if link_text =='/': continue
        if link_text == url: continue
        if link_text.endswith('/') :#directory, dig into it
            yield from get_links(pattern,link_text)
        else:
            yield link_text
        #links.append(link.get('href'))


def main():
    global URL
    URL= get_urls()[0].get('url')
    pattern ='Tamil'
    links = get_links(pattern)
    for i, link in enumerate(links):
        print("getting links inside url:",link)
        print(link)
        #if link == '/':
        #    continue
        #if i<8:
        #    print(get_links(url+link,pattern))

    #print (links)

if __name__ == "__main__":
    main()
