from collections import Counter

def count_common(words):
    """
    This function takes a dictionary where keys are unique identifiers and values are lists of strings.
    It returns the count of the most frequently occurring string across all lists in the dictionary.
    
    Parameters:
    - words (dict): A dictionary with string values.
    
    Returns:
    - int: The count of the most frequent string across all lists in the dictionary.
           If no strings are found, it returns 0.
    """
    if not isinstance(words, dict):
        raise TypeError("Input must be a dictionary.")
    
    # Extract words from dictionary values
    words_list = []
    for value in words.values():
        if isinstance(value, str):
            words_list.extend(value.split())
        else:
            raise TypeError("All dictionary values must be strings.")
    
    if not words_list:
        return 0
    
    # Count occurrences of each word
    word_counter = Counter(words_list)
    
    # Find the most common word and its count
    if word_counter:
        most_common_word, most_common_count = word_counter.most_common(1)[0]
        return most_common_count
    else:
        return 0