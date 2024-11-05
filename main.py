from bs4 import BeautifulSoup
import requests

class EventHost:
    def __init__(self, url, name, tag, class_):
        self.url = url
        self.name = name
        self.tag = tag
        self.class_ = class_

class Event:
    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url

class Scraper:
    ScrapedDataList = []
    def __init__(self):
        self.ScrapedDataList = []
        self.EventHostList = [
            EventHost("https://arenariga.com/", "ArenaRiga", "h3", "entry-title")
        ]
    def ScrapeList(self):
        self.ScrapedDataList = []
        for host in self.EventHostList:
            rawXML = requests.get(host.url).content
            self.ScrapedDataList.append(rawXML)
        return self.ScrapedDataList
    
class Formatter:
    def __init__(self, scraper):
        self.scraper = scraper
    def filterArticles(self):
        articles = []
        EventHostList = scraper.EventHostList
        structXML = BeautifulSoup(scraper.ScrapedDataList[0], "html.parser")
        rawArticles = structXML.find_all(EventHostList[0].tag, class_=EventHostList[0].class_)
        for i in rawArticles:
            articles.append(i.get_text().strip())

if __name__ == "__main__":
    print("Running as main")
    scraper = Scraper()
    formatter = Formatter(scraper=scraper)

    scraper.ScrapeList() # This happens before formatting (procedures instead of functions)
    print(scraper.ScrapedDataList)
    print(formatter.filterArticles())

"""
    rawXML = scraper.ScrapeList()
    structXML = BeautifulSoup(rawXML[0], "html.parser")
    rawArticles = structXML.find_all("h3", class_="entry-title")
    articles = []
    for i in rawArticles:
        articles.append(i.get_text().strip())
    print(articles)
    
"""