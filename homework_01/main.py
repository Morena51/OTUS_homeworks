"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    square_numbers = []
    for number in numbers:
        square_numbers.append(number ** 2)
    return square_numbers


def is_prime(number):
    if number <= 0 or not isinstance(number, int):
        return False
    divider = 2
    if number == 1:
        return True
    while number % divider != 0:
        divider += 1
    return divider == number


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    result = []
    if filter_type == 'even':
        return list(filter(lambda number: number % 2 == 0, numbers))
    elif filter_type == 'odd':
        return list(filter(lambda number: number % 2 != 0, numbers))
    elif filter_type == "prime":
        return list(filter(lambda number: is_prime(number), numbers))
    else:
        raise ValueError("A filter type not in ['odd','even', 'prime']")
