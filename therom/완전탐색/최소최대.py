from collections import deque

T=int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]


def bfs(x,y):
    visited[y][x]=True
    q=deque()
    q.append((y,x))
    while q:
        py,px=q.popleft()
        for i in range(4):
            nx=px+dx[i]
            ny=py+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if visited[ny][nx]==False:
                    visited[ny][nx]=True
                    answer[ny][nx]=answer[py][px]+testcase[ny][nx]
                    q.append((ny,nx))

    return answer







for i in range(T):
    n=int(input())
    testcase = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        put=list(map(int,input().split(" ")))
        testcase.append(put)
    for i in range(n):
        for j in range(n):
            if visited[j][i]==False:
                ans=bfs(i,j)


    print(ans)





