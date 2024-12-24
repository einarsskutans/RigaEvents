import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if root_path not in sys.path:
    sys.path.append(root_path)

import uniscraper as us
import csv

if __name__ == "__main__":
    print("Running as main")
    
    ArenaRiga = us.Host("Arēna Rīga", "https://arenariga.com")
    ArenaRiga.scrape()
    formatter = us.Formatter(ArenaRiga)
    events = formatter.extract_list(["h3", "div"], ["entry-title", "date"])
    events.append([])

    for i in range(len(events[0])):
        events[2].append("")
        events[1][i], events[2][i] = events[1][i].split(' • ')

    # Exporting to .csv file
    with open("examples/RigaEvents/RigaEvents.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for i in range(len(events[0])):
            writer.writerow([events[0][i], events[1][i], events[2][i]])