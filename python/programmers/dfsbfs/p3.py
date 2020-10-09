from collections import deque
from collections import Counter


class TransFormation:
    def __init__(self, begin, target, words):
        self.target = target
        self.begin = begin
        self.words = words
        self.graph = {begin: set()}
        self.graph.update({word: set() for word in words})
        self.visit = {key: False for key in self.graph.keys()}
        self.layer = {key: 0 for key in self.graph.keys()}

    def makeGraph(self):
        graph = self.graph
        for key in graph:
            for word in self.words:
                if len(Counter(key) - Counter(word)) == 1:
                    graph[key].add(word)
        return graph

    # 몇번의 layer인지를 파악
    def bfs(self):
        begin = self.begin
        graph = self.makeGraph()
        ans = []
        que = deque([begin])
        self.layer[begin] = 0
        while que:
            out = que.popleft()
            self.visit[out] = True
            for elm in graph[out]:
                if self.visit[elm] != True:
                    que.append(elm)
                    self.layer[elm] = self.layer[out] + 1
                if elm == self.target:
                    return self.layer[self.target]
        return self.layer[self.target]


def solution(begin, target, words):
    if target not in words:
        return 0
    t = TransFormation(begin, target, words)
    ans = t.bfs()
    return ans