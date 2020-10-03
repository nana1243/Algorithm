# 여기서 최적화 할 수 있는 방법?

from itertools import combinations
from collections import deque
from copy import deepcopy

n,m = map(int,input().split(" "))
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int,input().split(" ")))

print(board)


def bfs(start_x,start_y,b,visited):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    start=[start_x,start_y]

    que = deque([start])

    while que:
        cur_x,cur_y = que.popleft()
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]

            if 0<=new_x<m and 0<=new_y<n and b[new_y][new_x]==0 and visited[new_y][new_x]==False:
                b[new_y][new_x] = 2
                visited[new_y][new_x] = True
                que.append([new_x,new_y])
    return b



def safe(board):

    safe_guard=[]
    for i in range(n): #y
        for j in range(m): #x
            if board[i][j]==0 :
                safe_guard.append([j,i])

    c = deque(combinations(safe_guard,3))

    return c


def solution():
    c = safe(board)
    ans=0

    while c:
        b = deepcopy(board)

        visited = [[False for _ in range(m)] for _ in range(n)]

        first,second,third = c.popleft()
        b[first[1]][first[0]] =1
        b[second[1]][second[0]] =1
        b[third[1]][third[0]] =1
        cnt=0

        for i in range(n):
            for j in range(m):
                if b[i][j] ==2:
                    b=bfs(j,i,b,visited)

        for i in range(n):
            for j in range(m):
                if b[i][j]==0:
                    cnt+=1
        ans = max(cnt,ans)

    return ans



print(solution())