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
