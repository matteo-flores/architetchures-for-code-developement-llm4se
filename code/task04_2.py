from typing import *

def decimal_to_Octal(deciNum: int) -> int:
    """
    Converts a given decimal number to its octal representation.
    
    Args:
    deciNum (int): The decimal number to convert.
    
    Returns:
    int: The octal representation of the input decimal number.
    
    Raises:
    TypeError: If the input is not an integer.
    ValueError: If the input is greater than 255.
    """
    if not isinstance(deciNum, int):
        raise TypeError("Input must be an integer")
    if deciNum < 0:
        deciNum = abs(deciNum)
    if deciNum > 255:
        raise ValueError("Input must be less than or equal to 255")

    if deciNum == 0:
        return 0

    octal_str = ""  # Initialize an empty string to store the octal digits
    while deciNum > 0:  # Loop until the decimal number becomes zero
        remainder = deciNum % 8  # Calculate the remainder when dividing by 8
        octal_str += str(remainder)  # Append the remainder to the octal string
        deciNum //= 8  # Divide the decimal number by 8 and continue the loop

    return int(octal_str[::-1])  # Convert the octal string to an integer and reverse it