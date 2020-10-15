class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # TLE!!!!
        n = len(costs) // 2
        self.res = float('inf')

        def recur(a, b, curr, cost):
            if a == b == n:
                self.res = min(self.res, cost)
            if a > n or b > n:
                return
            l = len(curr)
            for i in range(l):
                new = curr[:i] + curr[i + 1:]
                recur(a + 1, b, new, cost + curr[i][0])
                recur(a, b + 1, new, cost + curr[i][1])

        recur(0, 0, costs, 0)
        return self.res

    def sol2(self, costs):
        n = len(costs) // 2
        refund = []
        cost = 0
        for i in range(2 * n):
            cost += costs[i][0]
            refund.append(costs[i][1] - costs[i][0])
        refund.sort()
        for i in range(n):
            cost += refund[i]
        return cost

