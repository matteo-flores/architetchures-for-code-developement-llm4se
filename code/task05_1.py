from collections import Counter

def count_common(words):
    """
    Write a function to count the most common words in a dictionary.

    Args:
        words: A list of strings representing words.

    Returns:
        A list of tuples, where each tuple contains a word and its count,
        sorted in descending order of count. If the input list is empty,
        an empty list is returned.
    """
    if not words:
        return []

    word_counts = Counter(words)
    return word_counts.most_common()