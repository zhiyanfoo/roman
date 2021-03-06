import math
import re
from lookup import INT_TO_ROMAN, ROMAN_TO_INT

"""
    @author: tmackenzie

"""

# used in roman_to_int
ROMAN_VALIDATE_RE = re.compile('^[M]{4,}')
ROMAN_GROUP_RE = re.compile('^([M]{0,3})([DCM]*)([XLC]*)([IVX]*)$')


def int_to_roman(input):
    """
       given an integer, input, that is greater than 0 and less than, 4000
       return its modern roman numeral represenation

    """

    if not 0 < input < 4000:
        raise ValueError("input must be between 1 and 3999")

    result = []

    """
        significant, is the significant digit of input..
        used to lookup dict.
            1 = ones.
            2 = tens.
            3 = hundreds
            4 = thousands.

        factor, is the whole number for the current significant digit.
        used to calculate, count.
            example, input = 101
            - factor = 100.

        count, the number of times input is divisible by factor.
        used to lookup the arabic, romans tuple.
            example, input = 101, factor = 100
            - count = 1

    """

    while input != 0:

        significant = int(math.log10(input)) + 1

        # this could have been a dict look-up, see branch factor_dict..
        factor = 10 ** (significant - 1)

        count = (input / factor)

        # acquire the arabic and roman values
        number, roman = INT_TO_ROMAN[significant][count]
        result.append(roman)

        # this could just be, count * factor, its not b/c of speed.
        input -= number

    return ''.join(result)


def roman_to_int(input):
    """
        Given a string that represents a roman numeral, then,
        return its integer value
    """

    input = input.upper()

    if ROMAN_VALIDATE_RE.match(input) or input == "NULLA":
        raise ValueError("input must be between I and MMMCMXCIX")

    parsed_input = ROMAN_GROUP_RE.match(input)

    if parsed_input is None:
        raise ValueError("Input must be a Roman Numeral")

    result = 0
    for roman_numeral in parsed_input.groups():
        try:
            result += ROMAN_TO_INT[roman_numeral]
        except KeyError:
            pass

    return result
