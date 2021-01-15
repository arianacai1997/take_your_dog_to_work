class Solution:
    # use a dfs to record visited and test if there is a circle: TLE
    # topological sort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {u: [] for u in range(numCourses)}
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            in_degree[u] += 1
            g[v].append(u)
        start = [u for u in range(numCourses) if in_degree[u] == 0]
        # result = []
        cnt = 0
        while start:
            u = start.pop()
            # result.append(u)
            cnt += 1
            for v in g[u]:
                in_degree[v] -= 1  # 帮它解决一个先决条件
                if in_degree[v] == 0:
                    start.append(v)
        return True if cnt == numCourses else False
