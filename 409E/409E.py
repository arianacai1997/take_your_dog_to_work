class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        largest_odd = 0
        ans = 0
        odd = 0
        for k in set(s):
            c = s.count(k)
            ans += c
            if c % 2:
                odd += 1
        return ans if odd <= 1 else ans - (odd-1)