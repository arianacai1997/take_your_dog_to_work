class Solution:
    def splitArray(self, nums, m: int) -> int:
        def count_subarray(target):
            ans = 1  # cautious!!! I start calculating the first sub
            total = 0
            for num in nums:
                total += num
                if total > target:  # split and have a new subarray
                    ans += 1
                    total = num  # recalc the sum
            return ans <= m

        # BS to look for a fit target
        low, high = max(nums), sum(nums)  # the largets bound
        while high > low:
            mid = (low + high) // 2
            if count_subarray(mid):  # the target is too large and we do not need m subs
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    s = Solution()
    print(s.splitArray([7,2,5,10,8], 2))
