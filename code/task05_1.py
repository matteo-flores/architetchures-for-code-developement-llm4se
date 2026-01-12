from collections import Counter

def count_common(words):
    """ Write a function to count the most common words in a dictionary. """
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Find the maximum frequency
    max_frequency = max(word_counts.values())
    
    # Collect all words with the maximum frequency
    most_common_words = [word for word, count in word_counts.items() if count == max_frequency]
    
    return most_common_words