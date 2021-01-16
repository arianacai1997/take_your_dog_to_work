class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y > X:
            res += 1
            if Y % 2:
                Y += 1
            else:
                Y /= 2
        return int(res + X - Y)

