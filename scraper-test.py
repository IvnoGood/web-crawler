# scraper-python.py
import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style

main = "fr.cornhub.website/"
UrlToScrape = 'https://fr.cornhub.website/model/gijs'
WordDictionnary = {}


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
            if word in WordDictionnary:
                # Increment count if word is already in the dictionary
                WordDictionnary[word] += 1
            else:
                # Initialize count to 1 if word is new
                WordDictionnary[word] = 1


def TF():
    ##
    print()


def scrape(main, UrlToScrape):
    # Target URL for scraping

    # Send a GET request to fetch the HTML content
    response = requests.get(UrlToScrape)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the title, text, and all links
    url = soup.find("meta", property="og:url")
    title = soup.find("meta", property="og:title")
    paragraphs = [p.get_text() for p in soup.find_all("p")]  # type: ignore
    links = [a.get('href') for a in soup.find_all('a', href=True)]

    if (title is None):
        title = soup.select_one('title').text  # type: ignore
        print("Not using meta tag for title")
    else:
        title = re.search(r'content="([^"]+)"',
                          str(title)).group(1)  # type: ignore

    if (url is None):
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

    return url, title, paragraphs, links


if __name__ == '__main__':
    url, title, paragraphs, links = scrape(main, UrlToScrape)
    SetWordDictionnary(paragraphs, WordDictionnary)
    print(WordDictionnary)
