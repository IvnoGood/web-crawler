"""     if (description == None):
        description = soup.find("meta", property="og:description")  # type: ignore
        print("Using second meta tag for description")
    elif (description == None):
        description = soup.select_one('p').text  # type: ignore
        print("Not using meta tag for description") """

"""
     if (title == None):
        title = soup.select_one('h1').text  # type: ignore
        print("Not using meta tag for url")
    """