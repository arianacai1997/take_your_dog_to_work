class Solution:
    def wordBreak(self, s: str, wordDict):
        # TLE
        """The problem of this code is that every time I find a good fit of a word, I have to re-combine other words.
        For instance, in the case catsanddogcatdog, ["cat", "cats", "and", "sand", "dog"], after getting the combination
        of cat+sand or cats+and, I should have directly get the result of dogcatdog, instead of re-searching for the indices
        for these three words."""
        res = []
        seen = {}
        visited = set()
        for i in range(len(s)):
            seen[i] = []

        def dp(i, cache):
            self.cnt += 1
            if i >= len(s):
                res.append(' '.join(cache))
                return
            if i in visited and not seen[i]:
                return
            if seen[i]:
                for w in seen[i]:
                    dp(i + len(w), cache + [w])
            else:
                visited.add(i)
                for w in wordDict:
                    x = len(w)
                    if s[i:i + x] == w:
                        seen[i].append(w)
                        dp(i + x, cache + [w])

        dp(0, [])
        return res

    def wordBreak2(self, s: str, wordDict):
        def dp(i, cache):
            if i in cache:
                return cache[i]
            if i >= len(s):
                return []
            res = []
            for w in wordDict:
                if not s[i:].startswith(w):
                    continue
                if len(w) == len(s) - i:
                    res.append(w)
                else:
                    rest = dp(i + len(w), cache)
                    for nxt in rest:
                        res.append(w + ' ' + nxt)
            cache[i] = res
            return res

        return dp(0, {})

s = Solution()
print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
