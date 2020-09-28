class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            # 2-digit first otherwise we have to deal with 0 (10#) and will split strs like 11# into aa
            # * a boolean has appeared lots of times recently
            s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))
        return s
