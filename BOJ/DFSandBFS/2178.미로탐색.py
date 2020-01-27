# n, m = map(int, input().split()
Y,X=7,7

matrix = [list(map(int, list(input()))) for _ in range(Y)]
check  = [[0 for i in range(X)] for _ in range(Y)]
answer  = [[0 for i in range(X)] for _ in range(Y)]

from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 초기 조건
q = deque()
cnt=0
# check[0][0]=1
def bfs(x,y,cnt):
    q.append((x,y))
    check[y][x] = 1
    answer[y][x] = cnt
    while q:
        x,y=q.popleft()
        # if nx !=x and ny !=y:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and ny>=0 and nx<X and ny<Y:
                if check[ny][nx]==0 and matrix[ny][nx]==1:
                    check[ny][nx]=1
                    answer[ny][nx]=answer[y][x]+1
                    q.append((nx,ny))


    return answer
from pprint import pprint
pprint(bfs(0,0,cnt)[Y-1][X-1]+1)

