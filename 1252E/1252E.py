class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = [0] * n
        col = [0] * m
        for r, c in indices:
            row[r] ^= 1
            col[c] ^= 1
        res = 0
        for i in range(n):
            for j in range(m):
                res += row[i]^col[j]
        return res