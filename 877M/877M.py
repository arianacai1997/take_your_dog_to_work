from functools import lru_cache
class Solution:
    def stoneGame(self, piles) -> bool:
        return True

    def stoneGame(self, piles):
        @lru_cache(None)
        def winner(curr, total):
            if len(curr) <= 2:
                return max(curr)
            # the opponent's choice
            first = winner(curr[1:], total - curr[0])
            last = winner(curr[:-1], total - curr[-1])
            return max(total - first, total - last)

        total = sum(piles)
        ans = winner(tuple(piles), total)
        return ans >= total / 2

