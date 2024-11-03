
WordDictionnary = {}
paragraphs = ["hi i am bob"]


def SetWordDictionnary(paragraphs, WordDictionnary):
    for paragraph in paragraphs:
        for word in paragraph.split():
            if not word.istitle():
                if word in WordDictionnary:
                    # Increment count if word is already in the dictionary
                    WordDictionnary[word] += 1
                else:
                    # Initialize count to 1 if word is new
                    WordDictionnary[word] = 1



SetWordDictionnary(paragraphs, WordDictionnary)
print(WordDictionnary)

