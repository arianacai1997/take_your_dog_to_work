class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotten = False
        q = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
                elif grid[i][j] == 1:
                    rotten = True
        if not rotten:
            return 0
        if not q:
            return -1
        while q:
            [a, b, c] = q.pop(0)

            if a > 0 and grid[a - 1][b] == 1:
                grid[a - 1][b] = 2
                q.append([a - 1, b, c + 1])
            if a < row - 1 and grid[a + 1][b] == 1:
                grid[a + 1][b] = 2
                q.append([a + 1, b, c + 1])
            if b > 0 and grid[a][b - 1] == 1:
                grid[a][b - 1] = 2
                q.append([a, b - 1, c + 1])
            if b < col - 1 and graid[a][b + 1] == 1:
                grid[a][b + 1] = 2
                q.append([a, b + 1, c + 1])
                print(4)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return c


