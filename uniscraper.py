# Module uniscraper.py. Built this little thing to make the scraping process for
# my perhaps future web-scraping projects a bit easier.
# The formatter takes in css tag and/or class (or a list of them) and formats
# the raw data from Host class accordingly.

import time
from bs4 import BeautifulSoup
import requests

class Host:  # The website
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.scraped_data = ""
        
    def scrape(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.scraped_data = response.content
            return self.scraped_data
        except requests.exceptions.RequestException as e:
            print(f"Error scraping {self.url}: {e}")
            return None
    
class Formatter:
    def __init__(self, host):
        self.host = host
        self.parsed_html = BeautifulSoup(host.scraped_data, "html.parser")

    def extract(self, element, css_class):
        data = self.parsed_html.find_all(element, class_=css_class)
        for i in range(len(data)):
            data[i] = " ".join(data[i].get_text().split())
        return data
    def extract_list(self, element_list, css_class_list):
        if len(element_list) != len(css_class_list):
            raise ValueError("element_list and _class_list must have the same length.")
        data_list = []
        for i in range(len(element_list)):
            data = self.parsed_html.find_all(element_list[i], css_class_list[i])
            for j in range(len(data)):
                data[j] = " ".join(data[j].get_text().split())
            data_list.append(data)
        return data_list

if __name__ == "__main__":
    print("\n\nRunning as uniscraper.py\nSee an example below.")
    host1 = Host("ArenaRiga", "https://arenariga.com/")
    host1.scrape()
    new_formatter = Formatter(host1)
    example_list = new_formatter.extract_list(["h3", "div"], ["entry-title", "date"])

    example_list.append([]) # For third element list split from "date"

    for i in range(len(example_list[1])):
        date_list = example_list[1]
        example_list[2].append(date_list[i][date_list[i].find("•")+2:])
        date_list[i] = date_list[i][:date_list[i].find("•")-1]
    for i in example_list:
        time.sleep(1)
        print("---")
        for j in i:
            print(j)
