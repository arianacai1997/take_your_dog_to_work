MAX_value = 999999


def dijkstra(graph, s):
    if graph is None:
        return None
    dist = [MAX_value] * len(graph)
    dist[s] = 0
    seen = []
    queue = [i for i in range(len(graph))]
    dist_init = [i for i in graph[s]]
    while queue:
        # find the node with min distance to s in queue
        u_dist = min([d for v, d in enumerate(dist_init) if v in queue])
        u = dist_init.index(u_dist)

        seen.append(u)
        queue.remove(u)

        for v, d in enumerate(graph[u]):
            if 0 < d < MAX_value:
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
                    dist_init[v] = dist[v]

    return dist


def dijkstra2(graph, s):
    dist = [float('inf') for i in range(len(graph))]
    dist[s] = 0
    q = []
    prev = {}
    for node in range(len(graph)):
        q.append([node, graph[s][node]])
    while q:
        v = None
        m = float('inf')
        for n, d in q:
            if d < m:
                m = d
                v = n
        q.remove([v, m])
        for u, e in enumerate(graph[v]):
            tmp = dist[v] + e
            if tmp < dist[u]:
                dist[u] = tmp
                prev[u] = v
    return dist, prev

        




if __name__ == '__main__':
    # graph_list[i]: the list of distances from node i to others
    graph_list = [[0, 9, MAX_value, MAX_value, MAX_value, 14, 15, MAX_value],
                  [9, 0, 24, MAX_value, MAX_value, MAX_value, MAX_value, MAX_value],
                  [MAX_value, 24, 0, 6, 2, 18, MAX_value, 19],
                  [MAX_value, MAX_value, 6, 0, 11, MAX_value, MAX_value, 6],
                  [MAX_value, MAX_value, 2, 11, 0, 30, 20, 16],
                  [14, MAX_value, 18, MAX_value, 30, 0, 5, MAX_value],
                  [15, MAX_value, MAX_value, MAX_value, 20, 5, 0, 44],
                  [MAX_value, MAX_value, 19, 6, 16, MAX_value, 44, 0]]

    distance = dijkstra(graph_list, 0)
    print(distance)
    print(dijkstra2(graph_list, 0))
