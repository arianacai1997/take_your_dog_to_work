class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        """For each (cardinal) direction, and for each coordinate (r, c)
        let's compute the count of that coordinate:
        the longest line of '1's starting from (r, c) and going in that direction.
        With dynamic programming, it is either 0 if grid[r][c] is zero, else it is 1 plus the count of the coordinate in
        the same direction. For example, if the direction is left and we have a row like 01110110, the corresponding
        count values are 01230120, and the integers are either 1 more than their successor, or 0.
        For each square, we want dp[r][c] to end up being the minimum of the 4 possible counts.
        At the end, we take the maximum value in dp."""
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[N] * N for i in range(N)]

        for m in mines:
            grid[m[0]][m[1]] = 0

        for i in range(N):
            l, r, u, d = 0, 0, 0, 0

            for j, k in zip(range(N), reversed(range(N))):
                l = l + 1 if grid[i][j] != 0 else 0
                if l < grid[i][j]:
                    grid[i][j] = l

                r = r + 1 if grid[i][k] != 0 else 0
                if r < grid[i][k]:
                    grid[i][k] = r

                u = u + 1 if grid[j][i] != 0 else 0
                if u < grid[j][i]:
                    grid[j][i] = u

                d = d + 1 if grid[k][i] != 0 else 0
                if d < grid[k][i]:
                    grid[k][i] = d

        res = 0

        for i in range(N):
            for j in range(N):
                if res < grid[i][j]:
                    res = grid[i][j]

        return res