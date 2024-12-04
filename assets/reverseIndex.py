import json
import os


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
            addedwords[word].append(link)  # check and add

    json_object = json.dumps(addedwords, indent=4)

    print("wrote to json")

    # Writing to sample.json
    with open(path, "w") as outfile:
        outfile.write(json_object)
