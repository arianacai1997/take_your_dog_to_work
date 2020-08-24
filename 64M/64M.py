from functools import lru_cache


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        table = [[0] * n for i in range(m)]
        table[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if i == 0:
                    table[i][j] = grid[i][j] + table[i][j-1]
                elif j == 0:
                    table[i][j] = grid[i][j] + table[i-1][j]
                else:
                    table[i][j] = grid[i][j] + min(table[i][j-1], table[i-1][j])
        return table[-1][-1]

    def minPathSum2(self, grid):
        m, n = len(grid), len(grid[0])
        @lru_cache
        def helper(i, j):
            item = grid[i][j]
            if i == j == 0:
                return item
            if i == 0:
                return item + helper(i, j - 1)
            if j == 0:
                return item + helper(i - 1, j)
            return item + min(helper(i, j - 1), helper(i - 1, j))

        return helper(m - 1, n - 1)
