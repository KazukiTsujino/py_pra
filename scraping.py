import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site = site
    
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "pickup" in url:
                news_url.append(url)

news_url = []
news = "https://news.yahoo.co.jp/"
Scraper(news).scrape()

with open("news.txt","w") as f:
    for url in news_url:
        f.write(url + "\n")

    