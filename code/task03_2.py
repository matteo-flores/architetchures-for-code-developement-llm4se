from typing import List

def sort_numbers(numbers: str) -> str:
    """Input is a space-delimited string of numerals from 'zero' to 'nine'.

    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    Args:
        numbers: A string containing space-delimited number words.

    Returns:
        A string with the number words sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('')
    ''
    >>> sort_numbers('nine zero two')
    'zero two nine'
    """

    # Map number words to their integer equivalents for sorting.
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    # Create an inverse map to convert sorted integers back to words.
    inverse_number_map = {v: k for k, v in number_map.items()}

    # Handle the edge case of an empty input string.
    if not numbers:
        return ""

    # Split the input string into a list of number words.
    number_words = numbers.split()
    # Convert the list of number words into a list of their integer values.
    integer_values = [number_map[word] for word in number_words]
    # Sort the list of integer values in ascending order.
    integer_values.sort()
    # Convert the sorted integer values back into their corresponding number words.
    sorted_number_words = [inverse_number_map[val] for val in integer_values]

    # Join the sorted number words back into a space-delimited string.
    return ' '.join(sorted_number_words)