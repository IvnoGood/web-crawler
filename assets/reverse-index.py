import json


addedwords = {}


def reverseIndex(listwords, link):
    for word in listwords:
        addedwords.setdefault(word, []).append(link)

# Serializing json
json_object = json.dumps(addedwords, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(addedwords)
