from bs4 import BeautifulSoup
import requests

class EventHost:
    def __init__(self, url, name, tag):
        self.url = url
        self.name = name
        self.tag = tag

class Event:
    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url

class Scraper:
    def __init__(self):
        self.ScrapedDataList = []
    def Scrape(self, EventHostList):
        return requests.get(EventHostList[0].url).text # Raw XML string

if __name__ == "__main__":
    print("Running as main")

    scraper = Scraper()
    testlist = [EventHost("https://arenariga.com/", "ArenaRiga", "p")]
    
    rawXML = scraper.Scrape(testlist)
    structXML = BeautifulSoup(rawXML, "html.parser")
    rawArticles = structXML.find_all("h3", class_="entry-title")
    
    print(rawArticles)
