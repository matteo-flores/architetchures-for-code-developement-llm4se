from collections import Counter
from typing import List

def count_common(words: List[str]) -> Counter:
    counter = Counter()
    for word in words:
        if isinstance(word, str):
            counter[word] += 1
    return counter