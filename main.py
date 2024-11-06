from bs4 import BeautifulSoup
import requests
import csv

class EventHost:
    def __init__(self, url, name, tagName, tagUrl, tagDate):
        self.url = url
        self.name = name

        self.tagName = tagName
        self.tagUrl = tagUrl
        self.tagDate = tagDate

class Event:
    def __init__(self, name, url, date, host):
        self.name = name
        self.url = url
        self.date = date
        self.host = host
    def __str__(self):
        return f"{self.name}\n{self.url}\n{self.host}"

class Scraper:
    ScrapedDataList = []
    def __init__(self):
        self.ScrapedDataList = []
        self.EventHostList = [
            EventHost("https://arenariga.com/", "ArenaRiga", ("h3", "entry-title"), ("a", "event_href"), ("div", "date"))
            #EventHost("https://www.liveriga.com/lv/3-pasakumi?csrf_token=1c1fbf0b3759d89d1dfd9e7259dce78a&dateFrom=06.11.2024&dateTill=", "LiveRiga", "h3", "card-title"),
            #EventHost("https://www.forumcinemas.lv/", "ForumCinemas", "span", "name-part")
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
        ArticleList = []
        EventHostList = self.scraper.EventHostList
        ScrapedDataList = self.scraper.ScrapedDataList

        for i in range(len(ScrapedDataList)):
            articles = []
            structXML = BeautifulSoup(ScrapedDataList[i], "html.parser")

            
            names = structXML.find_all(EventHostList[i].tagName[0], class_=EventHostList[i].tagName[1])
            urls = structXML.find_all(EventHostList[i].tagUrl[0], href=True, class_=EventHostList[i].tagUrl[1])
            dates = structXML.find_all(EventHostList[i].tagDate[0], class_=EventHostList[i].tagDate[1])

            for j in range(len(names)):
                article = Event(names[j].get_text().split(), urls[j]["href"], dates[j].get_text().split(), "dont")
                articles.append(article)

            ArticleList.append(articles)
        return ArticleList

if __name__ == "__main__":
    print("Running as main")
    mainScraper = Scraper()
    formatter = Formatter(scraper=mainScraper)

    mainScraper.ScrapeList() # This happens before formatting (procedures instead of functions)
    events = formatter.filterArticles()

    # Exporting to .csv file
    with open("RigaEvents.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for list in events:
            for i in list:
                writer.writerow([i.name, i.url, i.date, i.host])
