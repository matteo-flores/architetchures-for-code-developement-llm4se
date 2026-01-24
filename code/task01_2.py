from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if in a given list of numbers, any two numbers are closer to each other than
    a given threshold.

    Args:
        numbers: A list of floating-point numbers.
        threshold: The maximum allowed difference between two numbers to be considered "close".

    Returns:
        True if any two numbers in the list are closer than the threshold, False otherwise.

    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    n = len(numbers)
    # Iterate through all possible pairs of numbers in the list.
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the absolute difference between the current pair of numbers.
            # If the difference is less than the threshold, it means they are close.
            if abs(numbers[i] - numbers[j]) < threshold:
                return True  # Found a pair of close elements, return True immediately.
    # If no close elements were found after checking all pairs, return False.
    return False