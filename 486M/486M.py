class Solution:
    def PredictTheWinner(self, nums) -> bool:
        if len(nums) % 2 == 0:
            return True
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n-2, -1, -1):  # idx n-1 is filled with nums[n-1]
            for j in range(i+1, n):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0

    """This solution used the intuition that if our opponent's score is n, then our score is sum(nums) - n.
So for each iteration:

Pass the sum of nums summ
If There are only 2 numbers in nums - return max(nums)
Get opponents score for both condition
If first number is chosen choose_first
If last number is chosen choose_last
Return the maximum of the both scores we can get"""

    def PredictTheWinner2(self, nums) -> bool:
        total = sum(nums)
        if not len(nums) % 2:
            return True

        def count_score(curr, total):
            if len(curr) <= 2:
                return max(curr)
            # the opponent's choise
            start = count_score(curr[1:], total - curr[0])
            end = count_score(curr[:-1], total - curr[-1])
            return max(total - start, total - end)

        return count_score(nums, total) >= total / 2

    def PredictTheWinner3(self, nums) -> bool:
        if not len(nums) % 2:
            return True
        def winner(curr, s, e, turn):
            if s == e:
                return turn * curr[s]
            a = turn * curr[s] + winner(curr, s+1, e, -turn)
            b = turn * curr[e] + winner(curr, s, e-1, -turn)
            return turn * max(turn*a, turn*b)  # max 里*turn是因为ab里带turn有可能负
        return winner(nums, 0, len(nums)-1, 1) >= 0


