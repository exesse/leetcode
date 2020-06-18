"""Most common algorithms written in Python 3."""


def binary_search(sorted_list, value) -> int:
    """
    Function search for the position of given value in sorted list.
    Returns index if found.
    :param sorted_list: list
    :param value: int
    :return: int
    """
    start = 0
    end = len(sorted_list) - 1

    while start <= end:

        mid = (start + end) // 2

        if sorted_list[mid] < value:
            start = mid + 1

        elif sorted_list[mid] > value:
            end = mid - 1

        elif sorted_list[mid] == value:
            return mid


def rec_sum(numbers, x=0) -> int:
    """
    Function return the sum of given list using recursion.
    :param numbers: list, list of integers
    :param x: int, current sum
    :return: int, total sum
    """
    if len(numbers) == 0:
        return x
    x += numbers[0]
    numbers.pop(0)
    return rec_sum(numbers, x)


def rec_biggest(numbers, x=0):
    """
    Function uses recusrion to find biggest number in given list.
    :param numbers: list, list of integers
    :param x: int, current highest
    :return: int, the highest given
    """
    if len(numbers) == 0:
        return x
    elif numbers[0] >= x:
        x = numbers[0]
    numbers.pop(0)
    return rec_biggest(numbers, x)
