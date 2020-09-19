import collections

class Solution:

    def diagonalSort(self, mat):
        if len(mat) <= 1:
            return mat
        r, c = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(r):
            for j in range(c):
                d[i-j].append(mat[i][j])
        for k, v in d.items():
            v.sort()
        for i in range(r):
            for j in range(c):
                mat[i][j] = d[i-j].pop(0)
        return mat