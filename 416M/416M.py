class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        nums.sort()
        dp = {0: {0}}
        for i in range(1, len(nums)+1):
            this = set()
            this = this.union(dp[i-1])
            for k in dp[i-1]:
                if k + nums[i-1] == target:
                    return True
                elif k + nums[i-1] < target:
                    this.add(k+nums[i-1])
                else:
                    break
                dp[i] = this
        return False

    def canPartition2(self, nums):
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        nums.sort()
        dp = [False for i in range(target+1)]
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        return dp[target]



if __name__ == '__main__':
    s = Solution()
    print(s.canPartition2([1,11,5, 5]))
    print(s.canPartition2([100]))
    print(s.canPartition2([1,2,5]))
