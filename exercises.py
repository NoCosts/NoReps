import random


def find_summands(summ_value):
    """
    Generates a string representation of the summands that add up to the given summ_value.
    Parameters:
        summ_value (int): The value of the sum.
    Returns:
        str: A string representation of the summands and the sum in the format 'b + r = s',
             where b is the second summand, r is the first summand, and s is the summ_value.
    Example:
        >>> find_summands(12)
        '5 + 7 = 12'
    """
    s = str(summ_value)
    l = len(s) - 1
    r = random.randint(10 ** (l - 1), (10 ** l) - 1)
    b = summ_value - r
    return str(b) + ' + ' + str(r) + ' = ' + s


print(find_summands(5261))
