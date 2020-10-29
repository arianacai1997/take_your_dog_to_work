class Solution(object):
    # TLE!!! B/C not storing a table to refer
    # This is not dp at all! see there is nothing to repeat and dynamically refer to.
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        self.res = 0

        def dp(G, i, prof):
            if i >= len(group):
                return
            if G >= group[i]:
                if prof + profit[i] >= P:
                    self.res += 1
                dp(G - group[i], i + 1, prof + profit[i])
            dp(G, i + 1, prof)

        dp(G, 0, 0)
        return self.res % (10 ** 9 + 7)

    """Well, it is a Knapsack problem and my first intuition is dp.

dp[i][j] means the count of schemes with i profit and j members.

The dp equation is simple here:
dp[i + p][j + g] += dp[i][j]) if i + p < P
dp[P][j + g] += dp[i][j]) if i + p >= P

Don't forget to take care of overflow.

For each pair (p, g) of (profit, group), I update the count in dp.

Time Complexity:
O(NPG)

this is a three level knapsack problem,
dp[k][i][p] means the count of schemes with first k choices and i profit and j members. 
if i and j doesn't start from P/G-g and decreases to 0, you can't omit the first level of dp.

"""

    def profitableSchemes2(self, G, P, group, profit):
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(i + p, P)][j + g] += dp[i][j]
        return sum(dp[P]) % (10 ** 9 + 7)


