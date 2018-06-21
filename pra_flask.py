from flask import Flask, render_template
import urllib.request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')

def hello():
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
                    #print(url)
                    url_list.append(url)
    name = "User"
    url_list = []
    Scraper("https://news.yahoo.co.jp/").scrape()
    maped_list = map(str,url_list)
    maped_list = "\n".join(maped_list)
    yahoo_url = maped_list
    return render_template('layout.html', title='flask test',name=name,yahoo_url=yahoo_url) 

if __name__ == "__main__":
    app.run(debug=True)