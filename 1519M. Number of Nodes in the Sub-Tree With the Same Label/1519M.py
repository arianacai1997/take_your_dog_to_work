from collections import defaultdict, Counter


class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        # this method is general to a graph
        # seen = set()
        # g = defaultdict(list)
        # for a, b in edges:
        #     g[a] += [b]
        #     g[b] += [a]
        # ans = [1] * len(labels)
        # def dfs(node):
        #     cnt = Counter()
        #     if node not in seen:
        #         cnt[labels[node]] += 1
        #         seen.add(node)
        #         for child in g[node]:
        #             cnt += dfs(child)
        #         ans[node] = cnt[labels[node]]
        #     return cnt
        # dfs(0)
        # return ans

        # since it is a tree, we can remove duplication by checking if the child is         # the node's parent. eg. [0, 1] g = {0: [1], 1:[0]}is a parent-child                 # pair.Once we are checking 0's children, we go to 1. We recursively check
        # 1' children and avoid 0 by checking if 0 is 1's parent.
        def dfs(node, parent):
            cnt = Counter()
            cnt[labels[node]] += 1
            for child in g[node]:
                if child != parent:
                    cnt += dfs(child, node)
            ans[node] = cnt[labels[node]]
            return cnt

        g = defaultdict(list)
        ans = [1] * len(labels)
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]
        dfs(0, -1)
        return ans

