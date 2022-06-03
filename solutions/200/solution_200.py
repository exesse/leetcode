"""200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""


class Solution:
    """Contains functions needed to compute the result."""

    def dfs(self, grid, slice_index, value_index):
        """Walks over the graph left, right, down, up."""
        if slice_index < 0 or slice_index >= len(grid):
            return 0
        if value_index < 0 or value_index >= len(grid[slice_index]):
            return 0
        if grid[slice_index][value_index] == '0':
            return 0
        grid[slice_index][value_index] = '0'
        self.dfs(grid, slice_index, value_index - 1)
        self.dfs(grid, slice_index, value_index + 1)
        self.dfs(grid, slice_index - 1, value_index)
        self.dfs(grid, slice_index + 1, value_index)
        return 1

    def numIslands(self, grid):
        """Returns the number of islands."""
        if len(grid) == 0:
            return 0
        count_islands = 0
        for slice_index in range(len(grid)):
            for value_index in range(len(grid[slice_index])):
                if grid[slice_index][value_index] == "1":
                    count_islands += self.dfs(grid, slice_index, value_index)
        return count_islands
