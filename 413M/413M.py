class Solution:
    def numberOfArithmeticSlices(self, A):
        self.sum = 0
        dp = {}

        def slice(i):
            if i < 2:
                return 0
            res = 0
            s = 0
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                if i - 1 in dp:
                    res = dp[i - 1] + 1
                else:
                    res = slice(i - 1) + 1
                self.sum += res
                dp[i] = res
            else:
                slice(i - 1)
            return res

        slice(len(A) - 1)
        return self.sum
