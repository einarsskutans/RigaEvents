from bs4 import BeautifulSoup
import requests

class EventHost:
    def __init__(self, url, name, tag, class_):
        self.url = url
        self.name = name
        self.tag = tag
        self.class_ = class_

class Event:
    def __init__(self, name, url, host):
        self.name = name
        self.url = url
        self.host = host
    def __str__(self):
        return f"\n{self.name}\n{self.url}\n{self.host}"

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
            articles.append(Event(i.get_text().strip(), "/url/", EventHostList[0].name))
        return articles

if __name__ == "__main__":
    print("Running as main")
    scraper = Scraper()
    formatter = Formatter(scraper=scraper)

    scraper.ScrapeList() # This happens before formatting (procedures instead of functions)
    events = formatter.filterArticles()
    for i in events:
        print(i)       