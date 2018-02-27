from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

url = "thelogicalindian.com/news/"

def getNewsTitles(limit):
    page = urlopen(Request("https://" + url, headers={'User-Agent': 'Mozilla/5.0'}))
    soup = BeautifulSoup(page, 'html.parser')
    return '. '.join(map(lambda title: title.h4.a.string, soup.find_all('div', class_='article-title')[0:limit]))
