def decimal_to_Octal(deciNum: int) -> int:
    """Converts a decimal integer to its octal representation.

    Args:
        deciNum: The decimal integer to convert.

    Returns:
        The octal representation of the decimal integer as an integer.
    """
    if deciNum == 0:
        return 0  # Base case: 0 in decimal is 0 in octal.

    octal_digits = []  # List to store the octal digits.
    while deciNum > 0:
        remainder = deciNum % 8  # Get the remainder when divided by 8.
        octal_digits.insert(0, str(remainder))  # Insert the remainder at the beginning of the list.
        deciNum //= 8  # Integer division by 8 to get the next decimal value.

    # Join the octal digits and convert the resulting string to an integer.
    return int("".join(octal_digits))