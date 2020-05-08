from heapq import heappush
from heapq import heappop

INF = 1e9
n, m = map(int, input().split())
v = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    v[a-1].append([b-1, c])
    v[b-1].append([a-1, c])
x, y = map(int, input().split())

def dijkstra(depart, arrive):
    dist = [INF]*n
    pq = []
    heappush(pq, (0, depart))
    dist[depart] = 0
    while pq:
        cost, now = heappop(pq)
        if dist[now] < cost:
            continue
        for nxt, ncost in v[now]:
            ncost += cost
            if dist[nxt] > ncost:
                dist[nxt] = ncost
                heappush(pq, (ncost, nxt))
    return dist[arrive]

path1 = dijkstra(0, x-1) + dijkstra(x-1, y-1) + dijkstra(y-1, n-1)
path2 = dijkstra(0, y-1) + dijkstra(y-1, x-1) + dijkstra(x-1, n-1)
ans = min(path1, path2)
print(ans if ans < INF else "-1")


