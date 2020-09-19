class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def dp(left, remain):
            if left == 0:
                return 0 if remain > 0 else 1
            if (left, remain) in memo:
                return memo[(left, remain)]
            to_return = 0
            # the remaining sum range. If remain = 10, f = 11, then the range is [0, 9]
            # if remain = 10, f = 3, then the remaining sum range is [7, 9]
            # remain-f is to get the lower bound of the a choice b/c at this time we can choose in range [1, f],
            # but the remaining sum of a negative value is trivial, so we do not do such vain job.
            for k in range(max(0, remain-f), remain):
                to_return += dp(left-1, k)
            memo[(left, remain)] = to_return
            return to_return
        return dp(d, target) % (10**9 + 7)