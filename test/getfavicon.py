import requests
from bs4 import BeautifulSoup


def get_favicon_from_html(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        icon_link = soup.find('link', rel=lambda x: x and 'icon' in x.lower())

        if icon_link:
            icon_url = icon_link.get('href')
            if not icon_url.startswith(('http://', 'https://')):
                icon_url = f"{url.rstrip('/')}/{icon_url.lstrip('/')}"
            print(f"Favicon URL: {icon_url}")
            return icon_url
        else:
            print("No favicon link found in HTML.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
