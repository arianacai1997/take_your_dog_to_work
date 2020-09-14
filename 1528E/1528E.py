class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = [None] * len(indices)
        for i in range(len(indices)):
            l[indices[i]] = s[i]
        return ''.join(l)