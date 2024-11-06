import json
import random
import os


link = 'dad791a2e6e24c0cbb9839245906939c'

# Data to be written
listwords = {
    'The': 1, 'CornHub': 3, 'team': 1, 'is': 3, 'always': 2, 'updating': 1, 'and': 5, 'adding': 2, 'more': 2, 'corn': 3, 'videos': 1, 'every': 1, 'day.': 1, "It's": 1, 'all': 1, 'here': 1, '100%': 1, 'free': 3, 'corn.': 1, 'We': 2, 'have': 2, 'a': 2, 'huge': 1, 'CCC': 2, 'video': 1, 'selection': 1, 'that': 2, 'you': 2, 'can': 1, 'download': 1, 'or': 1, 'stream.': 1, 'the': 3, 'most': 1, 'complete': 1, 'revolutionary': 1, 'tube': 1, 'site.': 1,
    'offer': 1, 'streaming': 1, 'videos,': 1, 'photo': 1, 'albums,': 1, 'number': 1, '1': 1, 'popping': 1, 'community': 1, 'on': 1, 'net.': 1, "We're": 1, 'working': 1, 'towards': 1, 'features': 1, 'will': 1, 'keep': 1, 'your': 1, 'love': 1, 'for': 1, 'corno': 1, 'alive': 1, 'well.': 1, 'Send': 1, 'us': 1, 'feedback': 1, 'if': 1, 'any': 1, 'questions/comments.': 1, 'CO2': 1, 'Net': 1, 'Zero': 1, 'website': 1, '©': 1, 'CornHub.website,': 1, '2024': 1
}

addedwords = {}

path = "sample.json"


n = 3
for i in range(n):
    for word in listwords:
        """ if addedwords.get(word) is not None:
        print("already exists" + word)
        addedwords.append(link)

    else:
        print("no exist" + word)
        addedwords[word] = link  # type: ignore
         """
        addedwords.setdefault(word, []).append(link)
    link = random.randint(500, 1000)
# Serializing json
json_object = json.dumps(addedwords, indent=4)

if os.path.isfile(path):
    with open('sample.json', 'r') as openfile:
        # Reading from json file
        addedwords = json.load(openfile)
else:
    with open("sample.json", "w") as outfile:
    outfile.write(json_object)

# Writing to sample.json


print(addedwords)
