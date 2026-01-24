def decimal_to_Octal(deciNum: int) -> int:
    """ Convert a decimal number to its octal representation.

    >>> decimal_to_Octal(10)
    12
    >>> decimal_to_Octal(2)
    2
    >>> decimal_to_Octal(33)
    41
    """
    if deciNum == 0:
        return 0
    octalNum = 0
    power = 1
    while deciNum > 0:
        remainder = deciNum % 8
        octalNum += remainder * power
        deciNum //= 8
        power *= 10
    return octalNum