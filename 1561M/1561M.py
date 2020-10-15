class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort()
        n = len(piles) // 3
        res = 0
        # [1,2,3,4,5,6,7,8,9] always pile like the largest 2 + the smallest 1
        for i in range(len(piles)-2, len(piles)-2-n*2, -2):
            res += piles[i]
        return res