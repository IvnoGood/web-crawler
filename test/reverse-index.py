import json
import random
import os


links = [
    "https://fr.cornhub.website/video/ch6712a096af6eb",
    "https://fr.cornhub.website/contact",
    "https://fr.cornhub.website/contact/advertise",
    "https://fr.cornhub.website/video/ch05a284b79b71d",
    "https://fr.cornhub.website/",
    "https://fr.cornhub.website/legal/fairuse",
    "https://fr.cornhub.website/video/ch338e7aeae5bbc",
    "https://fr.cornhub.website/legal/terms",
    "https://fr.cornhub.website/legal/privacy",
    "https://fr.cornhub.website/model",
    "https://fr.cornhub.website/video/chcff2c0aa54f26",
    "https://fr.cornhub.website/contact",
    "https://fr.cornhub.website/contact/advertise",
    "https://fr.cornhub.website/",
    "https://fr.cornhub.website/legal/fairuse",
    "https://fr.cornhub.website/model/gijs",
    "https://fr.cornhub.website/legal/terms",
    "https://fr.cornhub.website/legal/privacy",
    "https://fr.cornhub.website/model",
    "https://fr.cornhub.website/contact/advertise",
    "https://fr.cornhub.website/",
    "https://fr.cornhub.website/legal/fairuse",
    "https://fr.cornhub.website/legal/terms",
    "https://fr.cornhub.website/legal/privacy",
    "https://fr.cornhub.website/model",
    "https://fr.cornhub.website/contact",
    "https://fr.cornhub.website/",
    "https://fr.cornhub.website/legal/fairuse",
    "https://fr.cornhub.website/legal/terms",
    "https://fr.cornhub.website/legal/privacy",
    "https://fr.cornhub.website/model",
    "https://fr.cornhub.website/contact",
    "https://fr.cornhub.website/contact/advertise",
    "https://fr.cornhub.website/",
    "https://fr.cornhub.website/legal/fairuse",
    "https://fr.cornhub.website/model/gijs",
    "https://fr.cornhub.website/legal/terms",
    "https://fr.cornhub.website/legal/privacy",
    "https://fr.cornhub.website/model",
    "https://fr.cornhub.website/model/cvideos",
    "https://fr.cornhub.website/video/ch6712a096af6eb",
    "https://fr.cornhub.website/video/chfe584ab6fa64a",
    "https://fr.cornhub.website/video/chc0b23fe5ebd56",
    "https://fr.cornhub.website/video/chb9844c42366b8",
    "https://fr.cornhub.website/video/ch30a3ecc6f1625",
    "https://fr.cornhub.website/model",
    "https://fr.cornhub.website/model/butteredcob",
    "https://fr.cornhub.website/model/cobbers",
    "https://fr.cornhub.website/video/ch8ff481b71afad",
    "https://fr.cornhub.website/video/ch338e7aeae5bbc",
    "https://fr.cornhub.website/contact",
    "https://fr.cornhub.website/model/popped",
    "https://fr.cornhub.website/legal/fairuse",
    "https://fr.cornhub.website/model/gijs",
    "https://fr.cornhub.website/legal/terms",
    "https://fr.cornhub.website/video/chc4b07bc66bda7",
    "https://fr.cornhub.website/video/ch58861e6f84de4",
    "https://fr.cornhub.website/video/ch2946eb16a1158",
    "https://fr.cornhub.website/contact/advertise",
    "https://fr.cornhub.website/model/yebdeb",
    "https://fr.cornhub.website/legal/privacy",
    "https://fr.cornhub.website/contact",
    "https://fr.cornhub.website/contact/advertise",
    "https://fr.cornhub.website/",
    "https://fr.cornhub.website/legal/terms",
    "https://fr.cornhub.website/legal/privacy",
    "https://fr.cornhub.website/model"
]

# Data to be written
listwords = {
    'The': 1, 'CornHub': 3, 'team': 1, 'is': 3, 'always': 2, 'updating': 1, 'and': 5, 'adding': 2, 'more': 2, 'corn': 3, 'videos': 1, 'every': 1, 'day.': 1, "It's": 1, 'all': 1, 'here': 1, '100%': 1, 'free': 3, 'corn.': 1, 'We': 2, 'have': 2, 'a': 2, 'huge': 1, 'CCC': 2, 'video': 1, 'selection': 1, 'that': 2, 'you': 2, 'can': 1, 'download': 1, 'or': 1, 'stream.': 1, 'the': 3, 'most': 1, 'complete': 1, 'revolutionary': 1, 'tube': 1, 'site.': 1,
    'offer': 1, 'streaming': 1, 'videos,': 1, 'photo': 1, 'albums,': 1, 'number': 1, '1': 1, 'popping': 1, 'community': 1, 'on': 1, 'net.': 1, "We're": 1, 'working': 1, 'towards': 1, 'features': 1, 'will': 1, 'keep': 1, 'your': 1, 'love': 1, 'for': 1, 'corno': 1, 'alive': 1, 'well.': 1, 'Send': 1, 'us': 1, 'feedback': 1, 'if': 1, 'any': 1, 'questions/comments.': 1, 'CO2': 1, 'Net': 1, 'Zero': 1, 'website': 1, '©': 1, 'CornHub.website,': 1, '2024': 1
}

addedwords = {}

path = "sample.json"


def reverseIndex(path, addedwords, listwords, link):
    # check if the json file exists
    if os.path.isfile(path):
        with open(path, 'r') as openfile:
            try:
                # Try reading from JSON file
                addedwords = json.load(openfile)
            except json.JSONDecodeError:
                print(
                    "The file contains invalid JSON. Initializing with an empty dictionary.")
                addedwords = {}
    else:  # if not generate a new one
        with open(path, "w") as outfile:
            print()

    # iterate through each word in the list
    # then check if the word is in the json
    # if not add a new one
    for word in listwords:
        if link not in addedwords.setdefault(word, []):
            addedwords[word].append(link)
  # check and add

    json_object = json.dumps(addedwords, indent=4)

    print(json_object)

    # Writing to sample.json
    with open(path, "w") as outfile:
        outfile.write(json_object)


for link in links:
    reverseIndex(path, addedwords, listwords, link)
