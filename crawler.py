# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

from pydantic_core import Url
import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse
import time
from unittest import result
import attr
import attrs
import re
from colorama import Fore, Style
import os
import json

main = "fr.cornhub.website/"
UrlToScrape = 'https://fr.cornhub.website/model/gijs'

filename = "0scraper.csv"
QueueLinks = []
AllLinks = []

WordDictionnary = {}


def is_url(s):
    try:
        result = urllib.parse.urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def ToCSV(filename, url, title, paragraphs):
    content = [url, title, paragraphs]
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(content)
        print("written !")


def CheckLinks(links, UrlToScrape, main):
    ValidLinks = set()
    for link in links:
        result = re.search(main, link)
        if result and link != UrlToScrape:
            ValidLinks.add(link)
            print(Fore.GREEN + "valid link: ", link)
        else:
            print(Fore.RED + "not valid link: ", link)
    return ValidLinks


def SetWordDictionnary(paragraphs, WordDictionnary):
    for paragraph in paragraphs:
        for word in paragraph.split():
            if not word.istitle():
                word[WordDictionnary] += 1


def scrape(main, UrlToScrape):
    # Target URL for scraping

    # Send a GET request to fetch the HTML content
    response = requests.get(UrlToScrape)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the title, text, paragraphs and all links
    url = soup.find("meta", property="og:url")
    title = soup.find("meta", property="og:title")
    paragraphs = [p.get_text() for p in soup.find_all("p")]  # type: ignore
    links = [a.get('href') for a in soup.find_all('a', href=True)]

    if (title == None):
        title = soup.select_one('title').text  # type: ignore
        print("Not using meta tag for title")
    else:
        title = re.search(r'content="([^"]+)"',
                          str(title)).group(1)  # type: ignore

    if (url == None):
        url = UrlToScrape
        print("Not using meta tag for url")

    links = CheckLinks(links, UrlToScrape, main)

    # Print extracted content
    print(Style.RESET_ALL)
    print("Curerent url:", url, '\n')
    print("Title:", title, '\n')
    print("paragraphs:", paragraphs, '\n')
    print("Links found on the page:")
    # print("disabled in code")
    for link in links:
        print(Fore.CYAN + link)
    print(Style.RESET_ALL + '\n')

    # return all the values for later use
    return url, title, paragraphs, links


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
        url, title, paragraphs, links = scrape(main, UrlToScrape)
        ToCSV(filename, url, title, paragraphs)
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
