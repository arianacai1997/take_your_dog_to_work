# lc 1192
"""tarjan(u){

　　DFN[u]=Low[u]=++Index // 为节点u设定次序编号和Low初值

　　Stack.push(u)   // 将节点u压入栈中

　　for each (u, v) in E // 枚举每一条边

　　　　if (v is not visted) // 如果节点v未被访问过

　　　　　　　　tarjan(v) // 继续向下找

　　　　　　　　Low[u] = min(Low[u], Low[v])  # v is from the subtree of u

　　　　else if (v in S) // 如果节点u还在栈内

　　　　　　　　Low[u] = min(Low[u], DFN[v])    # v is visited but in stack, 一定再回去visit v，所以看看DFN v和LOW u的大小

　　if (DFN[u] == Low[u]) // 如果节点u是强连通分量的根

　　repeat v = S.pop  // 将v退栈，为该强连通分量中一个顶点

　　print v

　　until (u== v)

}"""

import itertools


def strong_connect(vertex):
    global edges, indices, lowlinks, connected_components, index, stack
    indices[vertex] = index
    lowlinks[vertex] = index
    index += 1
    stack.append(vertex)

    for v, w in (e for e in edges if e[0] == vertex):
        if indices[w] < 0:  # DNF, means not visited
            strong_connect(w)
            lowlinks[v] = min(lowlinks[v], lowlinks[w])
        elif w in stack:
            lowlinks[v] = min(lowlinks[v], indices[w])

    if indices[vertex] == lowlinks[vertex]:
        connected_components.append([])
        while stack[-1] != vertex:
            connected_components[-1].append(stack.pop())
        connected_components[-1].append(stack.pop())
        print(connected_components[-1])


edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'),
         ('E', 'A'), ('A', 'E'), ('C', 'A'), ('C', 'E'),
         ('D', 'F'), ('E', 'F')]
vertices = set(v for v in itertools.chain(*edges))
# {'C', 'A', 'B', 'D', 'F', 'E'}

# {'F': -1, 'B': -1, 'E': -1, 'D': -1, 'A': -1, 'C': -1}
lowlinks = indices.copy()
# {'F': -1, 'B': -1, 'E': -1, 'D': -1, 'A': -1, 'C': -1}
connected_components = []

index = 0  # time index
stack = []
for v in vertices:
    if indices[v] < 0:
        strong_connect(v)

print(connected_components)

from collections import OrderedDict

matric = [[0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0]]
dfn = OrderedDict()
low = OrderedDict()
flag = dict()
count = 0
n = 6
num = 0

import collections


def criticalConnections2(self, n: int, connections: List[List[int]]) -> List[List[int]]:
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

                if low[v] > dfn[u]:  # lc1192 find the critical edges
                    res.append([u, v])
            elif v != parent[u]:  # means still in stack
                low[u] = min(low[u], dfn[v])

    for i in range(len(visited)):
        if not visited[i]:
            findBridge(i, visited, dfn, low, parent)
    return res
