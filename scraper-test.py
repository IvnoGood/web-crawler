# scraper-python.py
import requests
from bs4 import BeautifulSoup


def scrape():
    # Target URL for scraping
    url = 'https://quotes.toscrape.com/'

    # Send a GET request to fetch the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the title, text, and all links
    title = soup.select_one('').text  # type: ignore
    links = [a.get('href') for a in soup.find_all('a', href=True)]

    # Print extracted content
    print("Title:", title)
    print("Text:", text)
    print("Links found on the page:")
    for link in links:
        print(link)


if __name__ == '__main__':
    scrape()
