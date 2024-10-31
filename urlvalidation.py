import urllib.parse


def is_url(s):
    try:
        result = urllib.parse.urlparse(s)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


# Example usage:
print(is_url("http://example.com"))  # True
print(is_url("invalid_url"))
