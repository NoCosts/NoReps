import random


def find_summands(summ_value: int) -> str:
    """
    Generates a string representation of the summands that add up to the given summ_value.
    Parameters:
        summ_value (int): The value of the sum.
    Returns:
        str: A string representation of the summands and the sum in the format 'b + r = s',
             where b is the second summand, r is the first summand, and s is the summ_value.
    Example:
        >> find_summands(12)
        '5 + 7 = 12'

    Генерирует строковое представление слагаемых, которые дают заданное значение суммы.

    Аргументы:
        summ_value (int): Значение суммы.

    Возвращает:
        str: Строковое представление слагаемых в формате "первое_слагаемое + второе_слагаемое = сумма".
    """
    s = str(summ_value)
    l = len(s) - 1
    r = random.randint(10 ** (l - 1), (10 ** l) - 1)
    b = summ_value - r
    return str(b) + ' + ' + str(r) + ' = ' + s


def find_minuend_and_subtrahend(difference_value: int) -> str:
    """
    Generate a string representing a subtraction problem with a given difference value.
    Args:
        difference_value (int): The difference value for the subtraction problem.
    Returns:
        str: A string representing the subtraction problem in the format "minuend - subtrahend = difference".

    Генерирует строковое представление вычитания с заданным значением разности.

    Аргументы:
        difference_value (int): Значение разности для операции вычитания.

    Возвращает:
        str: Строковое представление операции вычитания в формате "уменьшаемое - вычитаемое = разность".

    """
    d = str(difference_value)
    l = len(d)
    s = random.randint(10 ** (l - 1), (10 ** l) - 1)
    m = s + difference_value
    return str(m) + ' - ' + str(s) + ' = ' + d


print(find_summands(526))
print(find_minuend_and_subtrahend(526))
