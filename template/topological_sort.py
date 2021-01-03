def topological(n: int, edges) -> bool:  # (u, v) in edges: v is the prerequesite for u: v->u
    g = {u: [] for u in range(n)}
    in_degree = [0] * n
    for u, v in edges:
        in_degree[u] += 1
        g[v].append(u)
    start = [u for u in range(n) if in_degree[u] == 0]
    result = []
    # cnt = 0
    while start:
        u = start.pop()
        result.append(u)
        # cnt += 1
        for v in g[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                start.append(v)  # can be traversed next time (finished all its prerequisites)
    # return True if cnt == n else False
    # Leetcode 207: if only need to output a boolean saying if there is a topo sort (without a circle)
    return result
