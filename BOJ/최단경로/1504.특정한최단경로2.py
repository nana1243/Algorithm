
import heapq
import sys

###### input ######

v,e =map(int,input().split(" "))
g =[[] for _ in range(v+1)]

## 여기서 방향성이 없다고 했기 때문에 양뱡향을 해줘야한다

for i in range(e):
    s,e,c=map(int,sys.stdin.readline.split(" "))
    g[s].append([e,c])
    g[e].append([s,c])

# 꼭지나가야할 정점
n,m = map(int,input().split(" "))

# ans[i]가 의미하는 것은 start에서 i까지 오는데 최소거리를 저장한다

def daikstra(start,end):
    ans=[INF]*(v+1)
    q=[]
    ans[start]=0
    heapq.heappush(q,[start,0])
    while q:
        # start의 -> start로 갈때, 최소의 거리를 뺸다 -> 그 뺀값이 mid이다
        now,cost = heapq.heappop(q)
        if ans[now]<cost:
            continue
        for nxt,ncost in g[now]:
            ncost+=cost
            if ans[nxt]>ncost:
                ans[nxt]=ncost
                heapq.heappush(q,[nxt,ncost])
    return ans[end]



answer1 = daikstra(0,n)+daikstra(n,m)+daikstra(m,v)
answer2 = daikstra(0,m)+daikstra(m,n)+daikstra(n,v)
