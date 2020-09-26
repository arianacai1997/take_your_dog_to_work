class Solution:
    def numDecodings(self, S):
        """Let's keep track of:

e0 = current number of ways we could decode, ending on any number;
e1 = current number of ways we could decode, ending on an open 1;
e2 = current number of ways we could decode, ending on an open 2;
(Here, an "open 1" means a 1 that may later be used as the first digit of a 2 digit number, because it has not been used in a previous 2 digit number.)

With the right idea of what to keep track of, our dp proceeds straightforwardly.

Say we see some character c. We want to calculate f0, f1, f2, the corresponding versions of e0, e1, e2 after parsing character c.

If c == '*', then the number of ways to finish in total is: we could put * as a single digit number (9*e0), or we could pair * as a 2 digit number 1* in 9*e1 ways, or we could pair * as a 2 digit number 2* in 6*e2 ways. The number of ways to finish with an open 1 (or 2) is just e0.

If c != '*', then the number of ways to finish in total is: we could put c as a single digit if it is not zero ((c>'0')*e0), or we could pair c with our open 1, or we could pair c with our open 2 if it is 6 or less ((c<='6')*e2). The number of ways to finish with an open 1 (or 2) is e0 iff c == '1' (or c == '2')."""
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

