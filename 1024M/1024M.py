class Solution:
    def videoStitching(self, clips, T: int) -> int:
        # Time O(NlogN), Space O(1)
        prev_end, end, res = -1, 0, 0
        for s, e in sorted(clips):
            if end >= T or s > end:
                break
            elif prev_end < s <= end:  # cut for start
                res += 1
                prev_end = end
            end = max(end, e)
        return res if end >= T else -1

    def videoStitching2(self, clips, T) -> int:
        """Loop on i form 0 to T,
loop on all clips,
If clip[0] <= i <= clip[1], we update dp[i]

Time O(NT), Space O(T)"""
        dp = [T + 1] * (T + 1)
        dp[0] = 0
        for i in range(1, T + 1):
            if dp[i - 1] < T:
                for c in clips:
                    if c[0] <= i <= c[1]:
                        dp[i] = min(dp[i], dp[c[0]] + 1)
        return dp[T] if dp[T] != T + 1 else -1

