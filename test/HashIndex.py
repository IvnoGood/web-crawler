import json
import uuid
import os

uuids = {}
link = 'https://www.CornHub.website'
path = "urlindex.json"

links = [
    "https://fr.cornhub.website/legal/fairuse",

]

"""   "https://fr.cornhub.website/",
"https://fr.cornhub.website/legal/privacy",
"https://fr.cornhub.website/model",
"https://fr.cornhub.website/legal/terms",
"https://fr.cornhub.website/contact/advertise" """


def HashIndex(uuids, links, path):
    # check if the json file exists
    if os.path.isfile(path):
        with open(path, 'r') as openfile:
            try:
                # Try reading from JSON file
                uuids = json.load(openfile)
            except json.JSONDecodeError:
                print(
                    "The file contains invalid JSON. Initializing with an empty dictionary.")
                uuids = {}
    else:  # if not generate a new one
        with open(path, "w") as outfile:
            print()

    # iterate through each word in the list
    # then check if the word is in the json
    # if not add a new one
    for link in links:
        if link not in uuids.setdefault(uuid.uuid4().hex, link):
            uid = uuid.uuid4().hex
            print(uid)
            uuids[uid] = link
            print(uuids)
            if link not in uuids.setdefault(uid, []):
                uuids[uid].append(link)

    # check and add
    # Save uuids to a JSON file
    with open(path, "w") as outfile:
        json.dump(uuids, outfile, indent=4)


HashIndex(uuids, links, path)
