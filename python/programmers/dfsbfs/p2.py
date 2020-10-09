from collections import deque


class Network:
    def __init__(self, n, computers):
        self.n = n
        self.computers = computers
        self.graph = {i: set() for i in range(1, n + 1)}
        self.visit = [False for _ in range(n + 1)]

    def makeGraph(self):
        computers = self.computers
        for i in range(len(computers)):
            for j in range(len(computers[i])):
                if i != j and computers[i][j] == 1:
                    self.graph[i + 1].add(j + 1)
                    self.graph[j + 1].add(i + 1)
        return self.graph

    def bfs(self, start):
        queue = deque([start])
        while queue:
            out = queue.popleft()
            self.visit[out] = True
            for elm in self.graph[out]:
                if self.visit[elm] == False:
                    queue.append(elm)
                    self.visit[elm] = True

    def countNetwork(self):
        graph = self.makeGraph()
        ans = 0
        for i in range(1, len(graph) + 1):
            if self.visit[i] == False:
                ans += 1
                self.bfs(i)

        return ans


def solution(n, computers):
    network = Network(n, computers)
    ans = network.countNetwork()

    return ans