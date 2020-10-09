from collections import defaultdict


class Graph:
    def __init__(self, tickets):
        self.tickets = tickets
        self.info = defaultdict(list)
        self.answer = []

    def makegraph(self):
        for location in self.tickets:
            start = location[0]
            end = location[1]
            self.info[start].append(end)
            self.info[start].sort(reverse=True)

    def dfs(self, via):
        if self.info[via] is None:
            return self.answer

        while self.info[via]:
            out = self.info[via].pop()
            self.dfs(out)
            self.answer.append(out)


def solution(tickets):
    g = Graph(tickets)
    g.makegraph()
    g.dfs("ICN")
    answer = ["ICN"] + g.answer[::-1]
    return answer