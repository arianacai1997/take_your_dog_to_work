class Solution:
    # top-down
    def minHeightShelves1(self, books, shelf_width: int) -> int:
        L = len(books)
        cache = {len(books): 0}

        def dp(start):
            if start in cache:
                return cache[start]
            cur_width = 0
            cur_height = 0
            ret = float("Inf")
            for i in range(start, L):
                cur_width += books[i][0]
                cur_height = max(cur_height, books[i][1])
                if cur_width > shelf_width:
                    break
                ret = min(ret, dp(i + 1) + cur_height)
            cache[start] = ret
            return ret
        return dp(0)

    # bottom-up
    def minHeightShelves2(self, books, shelf_width: int) -> int:
        L = len(books)
        dp = {i: float("Inf") for i in range(L)}
        dp[0] = books[0][1]
        dp[-1] = 0

        for i in range(1, L):
            print(i)
            cur_width, cur_height = books[i]
            dp[i] = cur_height + dp[i - 1]
            for j in range(i - 1, -1, -1):
                cur_width += books[j][0]
                cur_height = max(cur_height, books[j][1])
                if cur_width > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j - 1] + cur_height)
                print(dp)
            print()

        return dp[L - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minHeightShelves2([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))