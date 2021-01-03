class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # 题目理解：如果t太大了，那么frog停在leaf： it jumps forever on the same vertex
        # 如果t还有剩余并且它不在leaf，它必须往下跳，所以t=4，target=1，prob是0而不是1，因为它在root停不住
        if n == 1:
            return 1.0
        g = [[] for i in range(n + 1)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
        seen = [0] * (n + 1)

        def dfs(i, t):
            if i != 1 and len(g[i]) == 1 or t == 0:
                # g[i] == 1 means it is the leaf with one connected node (parent)
                # n=1已经判断了，所以target=1的时候，只能是t=0 prob才会是1
                return i == target
            seen[i] = 1
            res = sum(dfs(j, t - 1) for j in g[i] if not seen[j])
            return res / (len(g[i]) - (i != 1))
            # need to extract the parent node from the length. But the root does not have a parent

        return dfs(1, t)

