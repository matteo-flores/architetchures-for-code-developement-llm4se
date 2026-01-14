from typing import List

def find_last_occurrence(A: List[int], x: int) -> int:
    """
    This function finds the last occurrence of a given integer `x` in a list `A`.
    
    Parameters:
    A (List[int]): The input list of integers.
    x (int): The integer whose last occurrence needs to be found.
    
    Returns:
    int: The index of the last occurrence of `x` in `A`. If `x` is not found, returns -1.
    """
    last_index = -1  # Initialize the last index to -1
    for i in range(len(A) - 1, -1, -1):  # Iterate through the list in reverse order
        if A[i] == x:  # Check if the current element is equal to x
            last_index = i  # Update the last index to the current index
    return last_index  # Return the last index found