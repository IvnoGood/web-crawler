# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse
import time


root = "https://www.example.com"


def is_url(s):
    try:
        result = urllib.parse.urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def ToCSV(title, text, link):
    content = [title, text, link]
    with open('scraper.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(content)
        print("written !")


def scrape(root):
    url = root
    while True:
        response = requests.get(url)  # type: ignore
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data from the HTML
        title = soup.select_one('h1').text  # type: ignore
        text = soup.select_one('p').text  # type: ignore
        link = soup.select_one('a').get('href')  # type: ignore

        # Print extracted data
        print(title)
        print(text)
        print(link)

        # Save extracted data to CSV
        

        if is_url(url):
            url = link
            print(f"Url saved: {link}")
            print("\n")
        else:
            print("not valid")
            break
        time.sleep(1)
        # Update `url` if you want to continue scraping; otherwise, break loop
        # For example:
        # url = get_next_page_url(soup) if there's a next page link
        # break


if __name__ == '__main__':
    scrape(root)
