N=int(input())
M=int(input())
edge=[[]for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)




def bfs():
    bcheck=[0 for i in range(N+1)]
    banswer=[]
    q=[1]
    bcheck[1]=1
    while q:
        p=q.pop()
        banswer.append(p)
        for e in edge[p]:
            if bcheck[e]==0:
                bcheck[e]=1
                q.append(e)
    return len(banswer)-1

print(bfs())

