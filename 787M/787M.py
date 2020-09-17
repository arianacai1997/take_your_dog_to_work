from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights, src, dst, K) -> int:
        # TLE!!!!!
        self.res = float('inf')
        graph = defaultdict(list)
        for (s, e, w) in flights:
            graph[s].append([e, w])

        def bfs(start, curr, cost):
            if curr > K:
                return
            if curr <= K and start == dst:
                self.res = min(self.res, cost)
            for (v, w) in graph[start]:
                bfs(v, curr + 1, cost + w)

        bfs(src, -1, 0)
        return self.res if self.res < float('inf') else -1


    def findCheapestPrice(self, n, flights, src, dst, k):
        # dijkstra
        f = defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1




