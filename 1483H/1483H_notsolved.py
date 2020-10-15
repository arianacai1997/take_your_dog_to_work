class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log=math.ceil(math.log(n,2))
        self.dp=[[0]*self.log for _ in range(n)]
        self.depth=[0]*n
        g=[set() for _ in range(n)]
        for i in range(n):
            g[parent[i]].add(i)
        q=deque([0])
        while q:
            rmv=q.popleft()
            for i in g[rmv]:
                if parent[i]==rmv:
                    self.depth[i]=1+self.depth[rmv]
                    q.append(i)
        for h in range(self.log):
            for node in range(n):
                if h==0:
                    self.dp[node][h]=parent[node]
                else:
                    self.dp[node][h]=self.dp[self.dp[node][h-1]][h-1]
    def getKthAncestor(self, node: int, k: int) -> int:
        diff=self.depth[node]
        if diff<k:
            return -1
        for i in range(self.log):
            if ((k)&(1<<i))>0:
                node=self.dp[node][i]
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)