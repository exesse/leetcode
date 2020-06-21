"""Most common algorithms written in Python 3."""
from collections import deque


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


class BreadthFirstSearch:
    """"
    Breadth search. Finds closes way from start till the end.

    Test data set:

    graph = {
    "you" : ["alice", "bob", "claire"],
    "bob" : ["anuj", "peggy"],
    "alice" : ["peggy"],
    "claire" : ["thom", "jonny"],
    "anuj" : [],
    "peggy" : [],
    "thom" : [],
    "jonny" : []
    }
    """
    def __init__(self, graph):
        """
        Takes graph as input and start search from the point 'you'.

        :param graph: dict, input graph
        """
        self.graph = graph
        self.breadth_first_search('you')

    @staticmethod
    def person_is_seller(name):
        """
        Fake function to identify who is the seller by the last name letter.

        :param name: str, name for the comparison
        """
        return name[-1] == 'j'

    def breadth_first_search(self, name):
        """
        Actual search over the graph.

        :param name: str, the name of starting edge in the graph
        :return: Bool, true if person in graph and false if not
        """
        search_queue = deque()
        search_queue += self.graph[name]
        searched = []
        while search_queue:
            person = search_queue.popleft()
            if person not in searched:
                if self.person_is_seller(person):
                    print(f'found the seller it is {person}')
                    return True
                else:
                    search_queue += self.graph[person]
                    searched.append(person)
        return False


class Dijkstra:
    """
    Search for lowest cost in weighted graph.
    Doesn't work for negative weights.

    Test data:

    graph = {
        "start" : { "a": 6, "b" : 2},
        "a" : { "fin" : 1 },
        "b" : { "a" : 3, "fin" : 5},
        "fin" : {}
            }

    costs = {
        "a" : 6,
        "b" : 2,
        "fin" : float('inf')
            }

    parents = {
        "a" : "start",
        "b" : "start",
        "fin" : None
            }
    """
    def __init__(self, graph, costs, parents):
        self.processed = []
        node = self.find_lowest_cost_node(costs)
        while node is not None:
            cost = float(costs[node])
            neighbors = graph[node]
            for n in neighbors.keys():
                new_cost = cost + float(neighbors[n])
                if float(costs[n]) > new_cost:
                    costs[n] = new_cost
                    parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node(costs)

    def find_lowest_cost_node(self, costs):
        """
        Compares nodes costs.
        :param costs: dict, dict with costs values.
        """
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = float(costs[node])
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
