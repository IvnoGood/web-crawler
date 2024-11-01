# scraper-python.py
from unittest import result
import attr
import attrs
import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style

def CheckLinks(links, UrlToScrape):
    ValidLinks = set()
    for link in links:
        result = re.search("fr.cornhub.website/", link)
        if result and link != UrlToScrape:
            ValidLinks.add(link)
            print(Fore.GREEN + "valid link: ", link)
        else:
            print(Fore.RED + "not valid link: ", link)
    return ValidLinks


def scrape():
    # Target URL for scraping
    UrlToScrape = 'https://fr.cornhub.website/model/gijs'

    # Send a GET request to fetch the HTML content
    response = requests.get(UrlToScrape)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the title, text, and all links
    url = soup.find("meta", property="og:url")
    title = soup.find("meta", property="og:title")
    description = soup.find("p").getText() #type: ignore
    links = [a.get('href') for a in soup.find_all('a', href=True)]

    

    if (title == None):
        title = soup.select_one('title').text #type: ignore
        print("Not using meta tag for title")
    else:
        title = re.search(r'content="([^"]+)"', str(title)).group(1) #type: ignore

    if (url == None):
        url = UrlToScrape
        print("Not using meta tag for url")

    links= CheckLinks(links, UrlToScrape)


    # Print extracted content
    print(Style.RESET_ALL)
    print("Curerent url:", url, '\n')
    print("Title:", title, '\n')
    print("Description:", description, '\n')
    print("Links found on the page:")
    #print("disabled in code")
    for link in links:
        print(Fore.CYAN + link)
    print(Style.RESET_ALL + '\n')

if __name__ == '__main__':
    scrape()
