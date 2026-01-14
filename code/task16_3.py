from typing import List

def find_last_occurrence(A: List[int], x: int) -> int:
    """
    Find the index of the last occurrence of x in A.
    Returns -1 if x is not present.
    """
    # Iterate from the end so the first match is the last occurrence.
    for i in range(len(A) - 1, -1, -1):
        if A[i] == x:
            return i

    return -1