import json
import uuid
import os


def HashIndex(uuids, link, path):
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
    if link not in uuids.values():
        uid = uuid.uuid4().hex
        uuids[uid] = link
        if link not in uuids.setdefault(uid, []):
            uuids[uid].append(link)

    # check and add
    # Save uuids to a JSON file
    with open(path, "w") as outfile:
        json.dump(uuids, outfile, indent=4)

    return uid  # type: ignore
