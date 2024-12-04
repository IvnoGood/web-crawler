import requests


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


# Example usage
url = "https://fr.cornhub.website/model/gijs/favicon.ico"
is_valid_image_url(url)
