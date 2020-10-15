# bottom-up
def minScoreTriangulation(self, A):
    n = len(A)
    dp = [[0] * n for i in xrange(n)]
    for d in xrange(2, n):
        for i in xrange(n - d):
            j = i + d
            dp[i][j] = min(dp[i][k] + dp[k][j] + A[i] * A[j] * A[k] for k in xrange(i + 1, j))
    return dp[0][n - 1]


# top-down
def minScoreTriangulation2(self, A):
    memo = {}

    def dp(i, j):
        if (i, j) not in memo:
            memo[i, j] = min([dp(i, k) + dp(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
        return memo[i, j]

    return dp(0, len(A) - 1)