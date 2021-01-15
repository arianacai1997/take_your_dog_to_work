class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = set()
        co = grid[r0][c0]

        def dfs(r, c):
            if (r, c) in visited:
                return True

            if not (0 <= r < m and 0 <= c < n and grid[r][c] == co):
                return False

            visited.add((r, c))

            if dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1) < 4:
                grid[r][c] = color

            return True

        dfs(r0, c0)
        return grid

