def count_common(words):
    if not isinstance(words, dict):
        raise TypeError("Input must be a dictionary")
    values = words.values()
    if not values:
        return 0
    words_list = [word for word in values if isinstance(word, str) and word]
    counter = Counter(words_list)
    max_count = max(counter.values())
    return max_count