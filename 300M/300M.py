class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        l = len(nums)
        dp = [1 for i in range(l + 1)]
        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums) -> int:
        seq = list()
        for num in nums:
            flag = True
            for idx_in_seq, num_in_seq in enumerate(seq):
                if num <= num_in_seq:
                    seq[idx_in_seq], flag = num, False
                    print(seq)
                    print(num, num_in_seq)
                    break
            if flag:
                seq.append(num)
        return len(seq)

    def sol3(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        n = len(nums)
        s = []
        for i in range(n):
            if len(s) == 0 or s[-1] < nums[i]:
                s.append(nums[i])
            else:
                ans = -1
                l = 0
                r = len(s) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if s[mid] >= nums[i]:
                        ans = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                if ans != -1:
                    s[ans] = nums[i]
            print(s)
        return len(s)

if __name__ == '__main__':
    s = Solution()
    s.lengthOfLIS2([10,9,2,5,7,4,101,18,4.5,1])
    s.sol3([10, 9, 2, 5, 7, 4, 101, 18, 4.5, 1])

