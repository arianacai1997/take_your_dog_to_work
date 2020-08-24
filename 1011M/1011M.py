class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        def helper(target):
            ans = 1
            total = 0
            for w in weights:
                total += w
                if total > target:
                    ans += 1
                    total = w
            return ans <= D

        lo, hi = max(weights), sum(weights)
        while hi > lo:
            mid = (lo + hi) // 2
            if helper(mid):  # target is too large
                hi = mid
            else:
                lo = mid + 1
        return lo

if __name__ == '__main__':
    s = Solution()
    print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))