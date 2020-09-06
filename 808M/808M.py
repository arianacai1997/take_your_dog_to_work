class Solution:
    def soupServings(self, N: int) -> float:
        if N >= 4800:
            return 1
        N = -(-N//25)
        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            return (dp(a-4, b) + dp(a-3, b-1) + dp(a-2, b-2) + dp(a-1, b-3)) / 4
        return dp(N, N)

    def soupServings2(self, N):
        if N >= 4800:
            return 1
        N = -(-N//25)
        dp = [[1] * (N+1) for i in range(N+1)]  # dp[a][b]
        dp[0][0] = 0.5  # a = b =0
        for i in range(1, N+1):
            dp[i][0] = 0  # b = 0, the possibility is 0
        for a in range(1, N+1):
            for b in range(1, N+1):
                m = lambda x: max(0, x)   # to prevent the index from being negative!!!!!!!!!!!!!!!
                dp[a][b] = (dp[m(a-4)][b] \
                           + dp[m(a-3)][m(b-1)] \
                           + dp[m(a-2)][m(b-2)] \
                           + dp[m(a-1)][m(b-3)]) / 4
                if 1 - dp[a][b] < 1e-6: break  # shows how to break when sufficiently converged
            if 1 - dp[a][a] < 1e-6: break
        return dp[N][N]
