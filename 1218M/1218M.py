import collections

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # lolllll TLE!!!!!!!!!!!!
        if len(arr) == 1:
            return 1
        l = len(arr)
        dp = [1 for i in range(l + 1)]
        for i in range(1, l):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d, ans = collections.defaultdict(int), 0
        for num in arr:
            d[num] = d[num - difference] + 1
            ans = max(ans, d[num])
        return ans
