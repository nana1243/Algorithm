def solution(n, computers):
    adj = [[] for i in range(200)]
    for i in range(len(computers)):
        for j in range(len(computers)):
            if computers[i][j] == 1:
                adj[i + 1].append(j + 1)

    def bfs(adj, start):
        queue = []
        queue.append(start)
        checked[start] = True
        while queue:
            start = queue.pop(0)
            for w in adj[start]:
                if not checked[w]:
                    checked[w] = True
                    queue.append(w)

    checked = [False for i in range(0, len(computers) + 1)]
    cnt = 0
    for i in range(1, len(computers) + 1):
        if checked[i] != True:
            bfs(adj, i)
            cnt += 1

    return cnt