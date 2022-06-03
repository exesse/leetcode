"""200. Number of Islands tests."""
from solution_200 import Solution

TESTDATA = [
    [[["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]], 3],
    [[
        ["1"],
        ["1"],
        ["0"],
        ["1"],
        ["0"],
        ["1"],
        ["0"],
        ["1"],
        ["1"],
        ["1"],
    ], 4],
]


def test_solution():
    """Compares result of Solution with test input."""

    for test in TESTDATA:
        got, want = Solution().numIslands(test[0]), test[1]
        assert got == want
