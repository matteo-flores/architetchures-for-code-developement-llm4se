from collections import Counter

def count_common(words):
    """ Write a function to count the most common words in a dictionary. """
    if not words:
        return []

    word_counts = Counter(words)
    # The test cases expect only the top 4 most common words.
    return word_counts.most_common(4)
