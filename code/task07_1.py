from typing import List


def can_form_1974(digits: List[int]) -> str:
    """
    Given a list of four digits, determine whether they can be rearranged
    to form the sequence 1974.

    Return "YES" if possible, otherwise return "NO".

    >>> can_form_1974([1, 7, 9, 4])
    'YES'
    >>> can_form_1974([1, 1, 9, 4])
    'NO'
    """
    target = [1, 9, 7, 4]
    if sorted(digits) == sorted(target):
        return "YES"
    else:
        return "NO"
