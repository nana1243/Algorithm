from collections import deque

# 1. bfs 1 차원
### 하나의 그룹안의 원소 세기


n = int(input())
e = int(input())
g=[[]for _ in range(n+1)]
visit=[ False for _ in range(n+1)]

# 양방향 그래프
for i in range(e):
    s,e =map(int,input().split(" "))
    g[s].append(e)
    g[e].append(s)


def bfs(start):
    que=deque([start])
    visit[start]=True
    ans=0
    while que:
        p = que.popleft()
        for nxt in g[p]:
            if visit[nxt] == False:
                visit[nxt]=True
                ans+=1
                que.append(nxt)
    
    return ans



ans = bfs(1)
print(ans)

    

