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
