import sys
from heapq import heappop
from heapq import heappush

v,e = map(int,input().split(" "))

graph=[[] for _ in range(v+1)] # 주어진 그래프 생성할 리스트

for i in range(e):
    s,e,c = map(int,input().split(" "))
    graph[s].append([c,e])
    graph[e].append([c,s])
n,m =map(int,input().split(" "))

INF = sys.maxsize


def daikstra(start,target):
    dis = [INF for _ in range(v + 1)]
    dis[start]=0
    que=[]
    heappush(que, [0,start])
    while que:
        ccost,cur = heappop(que)
        for end in graph[cur]:
            if dis[end[1]]> ccost+ end[0]:
                dis[end[1]] = ccost+end[0]
                heappush(que,[dis[end[1]], end[1]])

    return dis[target]

ans1 = daikstra(1, n)+ daikstra(n,m)+ daikstra(m,v)

ans2 = daikstra(1, m)+ daikstra(m,n) + daikstra(n,v)

print(ans1)
print(ans2)


