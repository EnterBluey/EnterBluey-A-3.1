def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.

    Returns:
        tuple: (bool, int) - (True, characteristic) if valid, (False, 0) if invalid
    """
    try:
        float(num_string)

        if '.' in num_string:
            integer_part = num_string.split('.')[0]
        else:
            integer_part = num_string

        return True, int(integer_part)
    except:
        return False, 0


def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.

    Returns:
        tuple: (bool, int, int) - (True, numerator, denominator) if valid, (False, 0, 0) if invalid
    """
    try:
        float(num_string)

        if '.' not in num_string:
            return True, 0, 1

        fractional_part = num_string.split('.')[1]

        numerator = int(fractional_part)
        denominator = 10 ** len(fractional_part)

        return True, numerator, denominator
    except:
        return False, 0, 0
