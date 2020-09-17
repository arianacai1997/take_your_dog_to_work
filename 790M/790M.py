class Solution:
    def numTilings(self, N) -> int:
        # tile like { | | } in dp[i-2] will cause duplicate case with dp[i-1] case.
        # Consider this, { | | | } = { | } + { | | } ( which is dp[i-2] + { | | } ) is the same as { | | } + { | } ( which is dp[i-1] + { | } ) ,
        # so when only consider {二} when we think about dp[i-2].
        # https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116612/Easy-to-understand-O(n)-solution-with-Drawing-Picture-Explanation!
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 5:
            return 5
        dp = [0 for i in range(N + 1)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, N + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3] % (10 ** 9 + 7)
        return dp[N]