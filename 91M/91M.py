class Solution:
    # top-down TLE
    def numDecodings(self, s: str) -> int:
        self.res = 0

        def dp(idx):
            if idx >= len(s):
                self.res += 1
                return
            if s[idx] == '0':
                return
            if idx < len(s) - 1 and int(s[idx:idx + 2]) <= 26:
                dp(idx + 2)
            dp(idx + 1)

        dp(0)
        return self.res

    # bottom-up with a cache
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1:i]):  # (2)
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]

        return dp[-1]
