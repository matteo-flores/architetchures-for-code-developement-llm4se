from collections import Counter

def count_common(words):
    """
    Counts the most common words in a list of strings.
    
    Args:
    words (list): A list of strings to analyze.
    
    Returns:
    list: A list of tuples containing the most common words and their counts.
    """
    count = Counter()
    # Iterate over each word in the input list
    for word in words:
        # Check if the word is a string and contains only alphabetic characters
        if isinstance(word, str) and word.isalpha():
            # Convert the word to lowercase and increment its count in the counter
            count[word.lower()] += 1
    # Find the maximum count among all words
    max_count = max(count.values())
    # Filter the counter to include only words that have the maximum count
    return [(word, count) for word, count in count.items() if count == max_count]