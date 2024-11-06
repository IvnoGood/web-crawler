import urllib.parse


def is_url(links):
    for link in links:
        try:
            result = urllib.parse.urlparse(link)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
