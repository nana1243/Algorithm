from heapq import heappop
from heapq import heappush


class Hamilton:
    def __init__(self, n, costs):
        self.p = [i for i in range(n)]
        self.costs = costs
        self.n = n

    # u가 v의 조상이니?

    def find(self, u):
        if self.p[u] != u:
            u = self.find(self.p[u])
        return self.p[u]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)
        self.p[root2] = root1

    def returnAns(self):
        costs = self.costs
        costs.sort(key=lambda x: -x[2])
        ans = 0
        while costs:
            v1, v2, cost = costs[-1][0], costs[-1][1], costs[-1][2]
            if self.find(v1) != self.find(v2):
                ans += cost
                self.union(v1, v2)
            costs.pop()
        return ans


def solution(n, costs):
    h = Hamilton(n, costs)
    ans = h.returnAns()

    return ans