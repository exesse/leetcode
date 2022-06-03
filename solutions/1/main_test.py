"""1. Two Sum tests."""
from main import Solution

TESTDATA = [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[3, 2, 4], 6, [1, 2]],
        [[3, 3], 6, [0, 1]],
]


def test_solution():
    """Compares result of Solution with given input."""
    for test in TESTDATA:
        got, want = Solution().twoSum(test[0], test[1]), test[2]
        assert got == want
