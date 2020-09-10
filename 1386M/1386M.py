class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans = 0
        reserved = {}
        for s in reservedSeats:
            reserved[s[0]] = reserved.get(s[0], []) + [s[1]]
        for k, v in reserved.items():
            if len(v) == 1:
                ans += 2 if v[0] in [1, 10] else 1
            elif v == [1, 10]:
                ans += 2
            else:
                helper = [0] * 10
                for i in v:
                    helper[i - 1] = 1
                res = 0
                if helper[1:5] == [0, 0, 0, 0]:
                    res += 1
                if helper[5:9] == [0, 0, 0, 0]:
                    res += 1
                if res == 0 and helper[3:7] == [0, 0, 0, 0]:
                    res += 1
                ans += res
        return ans + 2 * (n - len(reserved))

