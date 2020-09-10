import collections


class Solution:
    def criticalConnections(self, n: int, connections):
        g = [[] for i in range(n)]
        self.index = 0
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        dfn = [None] * n  # also takes the role of seen set
        low = [None] * n
        res = []

        def tarjan(u, parent):
            dfn[u] = low[u] = self.index
            self.index += 1
            for v in g[u]:
                if not dfn[v]:
                    tarjan(v, u)
                    if dfn[u] < low[v]:
                        """
                        low[x] = essentially a strongly connected network defined by the earliest node...
            
                        dfn[u] < low[v]
                        if depth of recursion of u is earlier than the "network of v defined by the earliest node,"
                        then its guaranteed that v is not reachable without the existing connection.
                        必须先访问到u才能访问到v的network，所以u是必须的
                        
                        dfn[u] >= low[v]
                        if depth of recursion of u is later than or equal to the "network of v defined by the earliest node,"
                        we know that u comes later than the network, so it is reachable
                        不需要通过u到v，所以对v的那个network不重要
                        相等时，他们可以同时被访问到
                        """
                        res.append([u, v])
                if v != parent:  # 能从v到u，又能从parent到u，更新一条最短的
                    low[u] = min(low[v], low[u])

        tarjan(0, None)
        return res

    def criticalConnections2(self, n: int, connections):
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        dfn = [float('inf')] * n
        low = [float('inf')] * n
        visited = [False] * n
        parent = [float('inf')] * n

        self.Time = 1
        res = []

        def findBridge(u, visited, dfn, low, parent):

            visited[u] = True

            dfn[u] = self.Time
            low[u] = self.Time
            self.Time += 1

            for v in graph[u]:

                if not visited[v]:
                    parent[v] = u
                    findBridge(v, visited, dfn, low, parent)

                    low[u] = min(low[u], low[v])

                    if low[v] > dfn[u]:
                        res.append([u, v])

                elif v != parent[u]:
                    low[u] = min(low[u], dfn[v])

        for i in range(len(visited)):
            if not visited[i]:
                findBridge(i, visited, dfn, low, parent)
        con = collections.defaultdict(list)
        for i, x in enumerate(low):
            con[x].append(i)
        print(con.values())
        return res


s = Solution()
print(s.criticalConnections2(5, [[0, 2], [1, 4], [2, 3], [3, 4]]))
print(s.criticalConnections2(5, [[1, 0], [0, 2], [1, 4], [2, 3], [3, 4]]))
