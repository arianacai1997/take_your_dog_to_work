class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        ans = 10
        count = 9
        for i in range(1, n):
            count *= (10-i)
            ans += count
        return ans

    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        def solve(n):
            # n = 3, ans = 9(i=1)*9(i=2)*8(i=3)
            ans = 1
            for i in range(1, n + 1):
                if i == 1:
                    ans *= 9
                else:
                    ans *= 11 - i
            return ans

        if n == 0:
            return 1
        if n == 1:
            return 10
        dp = {0: 1, 1: 10}
        for i in range(2, n + 1):
            dp[i] = solve(i) + dp[i - 1]
        return dp[n]

    def countNumber(self, n):
        used = [0] * 10

        def backtrack(used, n, curr):
            print(curr, used)
            total = 1
            s = 1 if curr == 0 else 0
            # 各位不能为0
            for i in range(s, 10):
                if not used[i]:
                    used[i] = 1
                    if curr*10+i < 10 ** n:
                        total += backtrack(used, n, curr*10+i)
                    used[i] = 0
            print(total)
            return total
        return backtrack(used, n, 0)

s = Solution()
print(s.countNumbersWithUniqueDigits(2))
print(s.countNumbersWithUniqueDigits(8))
print(s.countNumber(2))
