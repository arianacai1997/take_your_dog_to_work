class Solution:
    # TEL!!! top-down
    def findSubstringInWraproundString(self, p: str) -> int:
        if len(p) <= 1:
            return len(p)
        table = [chr(ord) for ord in range(97, 97 + 26)]
        res = 0
        seen = set()
        for i in range(len(p)):
            if p[i] not in seen:
                res += 1
                seen.add(p[i])
            alp = table.index(p[i])
            for j in range(i + 1, len(p)):
                if table.index(p[j]) != (alp + 1) % 26:
                    break
                if p[i:j + 1] not in seen:
                    res += 1
                    seen.add(p[i:j + 1])
                alp = table.index(p[j])

        return res

    def findSubstringInWraproundString2(self, p: str) -> int:
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())