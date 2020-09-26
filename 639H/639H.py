class Solution:
    def numDecodings(self, S):
        MOD = 10 ** 9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in S:
            if c == '*':
                f0 = 9 * e0 + 9 * e1 + 6 * e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0

    def numDecodings2(self, s: str) -> int:
        ones = {str(i): 1 for i in range(1, 10)}
        ones['*'] = 9
        twos = {str(i): 1 for i in range(10, 27)}
        twos.update({'*' + str(i): 2 if i <= 6 else 1 for i in range(10)})
        twos.update({'1*': 9, '2*': 6, '**': 15})
        dp = 1, ones.get(s[0], 0)  # twos, ones/total
        MAX = 10 ** 9 + 7
        for i in range(1, len(s)):
            dp = dp[1], (ones.get(s[i], 0) * dp[1] + twos.get(s[i - 1: i + 1], 0) * dp[0]) % MAX
        return dp[-1]

