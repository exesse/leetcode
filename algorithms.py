"""Most common algorithms written in Python 3."""


def binary_search(sorted_list, value) -> int:
    """
    Function search for the position of given value in sorted list.
    Returns index if found. Time is: O(log(n)).
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


class SelectionSort:
    """
    Function performs sorting by selection.
    Average time is 0(n*n).
    """
    def __init__(self, array):
        self.array = array

    @staticmethod
    def smallest(array) -> int:
        """
        Function finds smallest value in given array.
        :param array: list, unsorted int list
        :return: int, index for lowest int in given list
        """
        low = array[0]
        low_index = 0
        for i in range(1, len(array)):
            if array[i] < low:
                low = array[i]
                low_index = i
        return low_index

    def sort(self) -> list:
        """
        Function generates new sorted list.
        :return result_array: list, new sorted list
        """
        result_array = []
        for i in range(len(self.array)):
            low = self.smallest(self.array)
            result_array.append(self.array.pop(low))
        return result_array


def quick_sort(array) -> list:
    """
    Function performs quick sort for average time:
                0(n*log(n))
    :param array: list, list of non sorted values
    :return: list, sorted list
    """
    if len(array) < 2:
        return array
    pivot = array[0]
    left_shoulder = [i for i in array if i < pivot]
    right_shoulder = [i for i in array if i > pivot]
    return quick_sort(left_shoulder) + [pivot] + quick_sort(right_shoulder)

