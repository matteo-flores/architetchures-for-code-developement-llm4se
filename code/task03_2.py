from typing import List

def sort_numbers(numbers: str) -> str:
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # Split the input string into a list of words
    number_list = numbers.split()

    # Convert the words to their corresponding integer values
    int_list = [number_dict[word] for word in number_list]

    # Sort the list of integers
    int_list.sort()

    # Convert the sorted integers back to words
    sorted_number_list = [list(number_dict.keys())[value] for value in int_list]

    # Join the sorted words into a single string separated by spaces
    sorted_numbers = ' '.join(sorted_number_list)

    return sorted_numbers