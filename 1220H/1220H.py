class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n <= 1:
            return n * 5
        # table = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        # dp[i][j] is the result ***end with*** the j-th vowel
        # idx_table = ['a', 'e', 'i', 'o', 'u']
        end_table = {0: [1, 2, 4], 1: [0, 2], 2: [1, 3], 3: [2], 4: [2, 3]}
        dp = [[0] * 5 for i in range(n+1)]
        for i in range(5):
            dp[1][i] = 1
        for i in range(2, n+1):
            for j in range(5):
                before = end_table[j]
                dp[i][j] = sum(dp[i-1][v] for v in before)
        return sum(dp[-1]) % (10**9 + 7)


    def countvowel(self, n):
        if n <= 1:
            return n * 5
        start_table = {0: [1], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [1]}
        dp = [[0] * 5 for i in range(n + 1)]
        for i in range(5):
            dp[1][i] = 1
        for i in range(2, n+1):
            for j in range(5):
                after = start_table[j]
                dp[i][j] = sum(dp[i-1][v] for v in after)
        return sum(dp[-1]) % (10**9 + 7)

    def count_vowel_permutations(n):
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10 ** 9 + 7)


