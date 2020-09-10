class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1:
            return 0
        if len(s) == 2:
            return 0 if s[0] == s[1] else 1
        n = len(s)
        isPal = [[False] * n for i in range(n)]
        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                if s[start] == s[end]:
                    isPal[start][end] = True if end - 1 <= start + 1 else isPal[start + 1][end - 1]
        minCut = [float('inf')] * (n + 1)
        minCut[0] = 0
        minCut[-1] = -1
        for end in range(1, n):
            for start in range(end + 1):
                if isPal[start][end]:
                    minCut[end] = min(minCut[start], minCut[end - 1] + 1)
                    # start<->end is in a part so there is no need to have extra cut after cutting at start. Also, end can be a separeted element apart from the end-1
        return minCut[n - 1]
