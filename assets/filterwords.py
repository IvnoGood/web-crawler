def filter_words_from_file(file_path, listwords):
    filtered_words = []  # List to hold words that are not in listwords
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
                    if word not in listwords:
                        # Add word if it's not a stop word
                        filtered_words.append(word)
                    else:
                        # Optional: See filtered words
                        print(f"Filtered out: {word}")
                        del listwords[word]
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

    print("Words not filtered:", filtered_words)
    return filtered_words
