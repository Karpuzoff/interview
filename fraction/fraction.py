
__author__ = "Valery Karpuzoff"
__copyright__ = "Copyright (C) 2015 Valery Karpuzoff"


def _digit_to_symbol(digit):
    return "0123456789ABCDEF"[digit]


def _convert_integer_to_string(number, base):
    if number == 0:
        return "0"
    string = ""
    while number != 0:
        digit = number % base
        string = _digit_to_symbol(digit) + string
        number //= base
    return string


def _convert_float_part_to_string(numerator, denominator, base):
    numerator %= denominator
    if numerator == 0:
        return ""

    string = '.'
    n = numerator

    remainder_to_index = dict()  # remainder : current length of string
    if n < denominator:
        remainder_to_index[n] = len(string)

    while n != 0:

        digit = n // denominator

        while digit == 0:
            n *= base
            digit = n // denominator
            if digit == 0 and string:
                string += '0'

            remainder_to_index[n] = len(string)
        n -= denominator * digit

        string += _digit_to_symbol(digit)

        if n not in remainder_to_index:
            remainder_to_index[n] = len(string)
        else:
            index = remainder_to_index[n]
            string = string[:index] + '(' + string[index:] + ')'
            break

    return string


def to_string(numerator, denominator, base=10):
    if denominator == 0:
        raise ValueError("Denominator cannot be equal to zero")
    if base < 2 or base > 16:
        raise ValueError("Invalid base. Valid value range: [2; 16]")

    result = ""
    if (numerator < 0) != (denominator < 0):
        result = '-'
    numerator = abs(numerator)
    denominator = abs(denominator)

    result += _convert_integer_to_string(numerator // denominator, base)
    result += _convert_float_part_to_string(numerator, denominator, base)
    return result


###############################################################################


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Usage: fraction <numerator> <denominator> [base=10]")
        exit(0)

    try:
        numerator = int(sys.argv[1])
        denominator = int(sys.argv[2])
        base = 10
        if len(sys.argv) == 4:
            base = int(sys.argv[3])
    except ValueError:
        print("All arguments must be integer numbers")
    else:

        try:
            print(to_string(numerator, denominator, base))
        except ValueError as error:
            print("Error: " + error.args[0])
            print("Abort")
        except Exception as error:
            print("Unexpected error: " + error.args[0])
            print("Abort")
