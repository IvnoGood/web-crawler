import os
import json


def TFIDF(path, addedwords, uuid, lisofwords):
    # Check if the file exists
    if os.path.isfile(path):
        with open(path, 'r') as openfile:
            try:
                # Try reading from JSON file
                addedwords = json.load(openfile)
            except json.JSONDecodeError:
                print(
                    "The file contains invalid JSON. Initializing with an empty dictionary.")
                addedwords = {}
    else:
        # Initialize an empty dictionary if file doesn't exist
        addedwords = {}
    addedwords[uuid] = lisofwords
    # Convert dictionary to JSON
    json_object = json.dumps(addedwords, indent=4)

    # Write to sample.json
    with open(path, "w") as outfile:
        outfile.write(json_object)

    print(json_object)
