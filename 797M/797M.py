class Solution:
    def allPathsSourceTarget(self, graph):
        res = []

        def dfs(idx, curr):
            if idx == len(graph) - 1:
                # deep copy!!!
                res.append(curr[:])
                return
            for j in graph[idx]:
                curr.append(j)
                dfs(j, curr)
                curr.pop()

        dfs(0, [0])
        return res
