class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    # either the starting of the string or
                    # the previous combination works
                    d[i] = True
        return d[-1]

    def wordBreak(self, s, wordDict):
        start = 0
        stack = [start]
        visited = set()
        while stack:
            start = stack.pop()
            if start in visited:
                continue
            visited.add(start)
            for word in wordDict:
                if s[start:].startswith(word):
                    x = len(word)
                    if x == len(s[start:]):
                        return True
                    stack.append(start + x)
        return False