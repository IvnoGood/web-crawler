# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import csv
import time
from colorama import Fore, Style
import os

# not used: from .assets.HashIndex import HashIndex #get the hash for the link
# activate when needed: from .assets.urlvalidation import is_url
from .assets.scraper import scrape
from .assets.scraper import SetWordDictionnary
from .assets.CsvAppend import ToCSV
from .assets.reverseIndex import reverseIndex


main = "fr.cornhub.website/"
UrlToScrape = 'https://fr.cornhub.website/model/gijs'

filename = "0scraper.csv"
QueueLinks = []
AllLinks = []

WordDictionnary = {}


jsonpath = 'index.json'
addedwords = {}

def Crawler(links, QueueLinks, UrlToScrape):
    print(QueueLinks)
    print()
    for link in links:
        if link not in AllLinks:
            if link not in QueueLinks:
                QueueLinks.append(link)
            else:
                print(Fore.RED + "Already in Queue: " + link + Style.RESET_ALL)
        else:
            print(Fore.RED + "Already Scraped: " + link + Style.RESET_ALL)
    if not QueueLinks:
        print("Crawl Finished")
        print("Exiting program now...")
        exit()

    UrlToScrape = QueueLinks[0]
    print(QueueLinks)
    print()
    del QueueLinks[0]
    print(QueueLinks)
    print()
    return QueueLinks, UrlToScrape


if __name__ == '__main__':

    if os.path.isfile("./" + filename):
        filename = str(int(filename[0])+1) + filename[1:len(filename)]

    with open(filename, mode='a', newline=''):
        # identifying header
        header = ['Url', 'title', 'paragraphs']

        writer = csv.DictWriter(
            open(filename, mode='w', newline=''), fieldnames=header)

        # writing data row-wise into the csv file
        writer.writeheader()
    while True:
        url, title, paragraphs, links = scrape(main, UrlToScrape) #save from the scrap url links etc...
        ToCSV(filename, url, title, paragraphs) #save to the csv file all the data
        SetWordDictionnary(paragraphs, WordDictionnary)
        
        for link in links:
            reverseIndex(jsonpath, addedwords, WordDictionnary, link)

        QueueLinks, UrlToScrape = Crawler(links, QueueLinks, UrlToScrape)
        time.sleep(5)


""" if is_url(url):
            url = link
            print(f"Url saved: {link}")
            print("\n")
        else:
            print("not valid")
            break
        time.sleep(1) """
