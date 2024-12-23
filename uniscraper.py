from bs4 import BeautifulSoup
import requests
import csv

class Host:  # Website
    def __init__(self, name, url, taglist):
        self.name = name
        self.url = url

        self.taglist = taglist

        self.ScrapedData = ""
    def scrape(self):
        self.ScrapedData = requests.get(self.url).content 
        return self.ScrapedData
    
class Formatter:
    def __init__(self, scraper):
        self.scraper = scraper
    
#names = structXML.find_all(EventHostList[i].tagName[0], class_=EventHostList[i].tagName[1])
#urls = structXML.find_all(EventHostList[i].tagUrl[0], href=True, class_=EventHostList[i].tagUrl[1])
#dates = structXML.find_all(EventHostList[i].tagDate[0], class_=EventHostList[i].tagDate[1])


if __name__ == "__main__":
    print("Running as uniscraper.py")
    host1 = Host("ArenaRiga", "https://arenariga.com/", [("h3", "entry-title"), ("a", "event_href"), ("div", "date")])
    
