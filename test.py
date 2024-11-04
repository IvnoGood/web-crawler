def filter_words_from_file(file_path, listwords):
    filtered_words = []
    try:
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into words
                words = line.split()
                for word in words:
                    # Remove punctuation and convert to lowercase
                    word = word.strip('.,!?()[]{}"\'').lower()
                    # Filter out the word if it's a stop word
                    print(word)
                    if word in listwords:  # and word not
                        filtered_words.append(word)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    return filtered_words


# Example usage
listwords = {'The': 1, 'CornHub': 3, 'team': 1, 'is': 3, 'always': 2, 'updating': 1, 'and': 5, 'adding': 2, 'more': 2, 'corn': 3, 'videos': 1, 'every': 1, 'day.': 1, "It's": 1, 'all': 1, 'here': 1, '100%': 1, 'free': 3, 'corn.': 1, 'We': 2, 'have': 2, 'a': 2, 'huge': 1, 'CCC': 2, 'video': 1, 'selection': 1, 'that': 2, 'you': 2, 'can': 1, 'download': 1, 'or': 1, 'stream.': 1, 'the': 3, 'most': 1, 'complete': 1, 'revolutionary': 1, 'tube': 1, 'site.': 1,
             'offer': 1, 'streaming': 1, 'videos,': 1, 'photo': 1, 'albums,': 1, 'number': 1, '1': 1, 'popping': 1, 'community': 1, 'on': 1, 'net.': 1, "We're": 1, 'working': 1, 'towards': 1, 'features': 1, 'will': 1, 'keep': 1, 'your': 1, 'love': 1, 'for': 1, 'corno': 1, 'alive': 1, 'well.': 1, 'Send': 1, 'us': 1, 'feedback': 1, 'if': 1, 'any': 1, 'questions/comments.': 1, 'CO2': 1, 'Net': 1, 'Zero': 1, 'website': 1, '©': 1, 'CornHub.website,': 1, '2024': 1}
file_path = "stopwords.txt"
filtered_words = filter_words_from_file(file_path, listwords)
print(filtered_words)
