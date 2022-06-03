// package solution200 | https://leetcode.com/problems/number-of-islands
// 200. Number of Islands
// Given an m x n 2D binary grid grid which represents a map of '1's (land) and
// '0's (water), return the number of islands.
// An island is surrounded by water and is formed by connecting adjacent lands
// horizontally or vertically. You may assume all four edges of the grid are all
// surrounded by water.
//
// Example 1:
// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
//
// Example 2:
// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3
//
// Constraints:
//     m == grid.length
//     n == grid[i].length
//     1 <= m, n <= 300
//     grid[i][j] is '0' or '1'.
package solution200

const (
	zero = 48
	one  = 49
)

// numIslands returns the number pf islands.
func numIslands(grid [][]byte) int {
	if len(grid) == 0 {
		return 0
	}
	var countIslands int
	for sliceIndex, slice := range grid {
		for valueIndex, value := range slice {
			if value == one {
				countIslands += dfs(&grid, sliceIndex, valueIndex)
			}
		}

	}
	return countIslands
}

// dfs walks over the graph left, right, down and up and flips ones to zero.
func dfs(grid *[][]byte, sliceIndex, valueIndex int) int {
	if sliceIndex < 0 || sliceIndex >= len((*grid)) {
		return 0
	}
	if valueIndex < 0 || valueIndex >= len((*grid)[sliceIndex]) {
		return 0
	}
	if (*grid)[sliceIndex][valueIndex] == zero {
		return 0
	}
	(*grid)[sliceIndex][valueIndex] = zero
	dfs(grid, sliceIndex, valueIndex+1)
	dfs(grid, sliceIndex, valueIndex-1)
	dfs(grid, sliceIndex+1, valueIndex)
	dfs(grid, sliceIndex-1, valueIndex)
	return 1
}
