import requests
from bs4 import BeautifulSoup


def is_valid_image_url(url):
    try:
        # Send a HEAD request to check headers without downloading the content
        response = requests.head(url, allow_redirects=True)

        # Check if the request was successful
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type')

            # Check if the Content-Type is an image
            if content_type and 'image' in content_type.lower():
                print(f"Valid image URL: {url}")
                return True
            else:
                print(f"URL is not an image: {
                      url} (Content-Type: {content_type})")
                return False
        else:
            print(f"Failed with status code: {response.status_code}")
            return False

    except requests.RequestException as e:
        print(f"Error while checking URL: {e}")
        return False


def get_favicon_from_html(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        icon_link = soup.find(
            'link', rel=lambda x: x and 'icon' in x.lower())  # type: ignore

        if icon_link:
            icon_url = icon_link.get('href')  # type: ignore
            if not icon_url.startswith(('http://', 'https://')):  # type: ignore
                # type: ignore
                # type: ignore
                icon_url = f"{url.rstrip('/')}/{icon_url.lstrip('/')}" # type: ignore
            print(f"Favicon URL: {icon_url}")
            if is_valid_image_url(icon_url):
                return icon_url
            else:
                return None
        else:
            print("No favicon link found in HTML.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
