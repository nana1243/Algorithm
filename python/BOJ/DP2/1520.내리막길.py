import sys
n,m=map(int,sys.stdin.readline().split(" "))
test=[]

for i in range(n):
    input=list(map(int,sys.stdin.readline().split(" ")))
    test.append(input)

check  = [[0 for i in range(m)] for _ in range(n)]
answer  = [[0 for i in range(m)] for _ in range(n)]

from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 초기 조건
q = deque()

def bfs():
    x,y=0,0
    q.append([x,y])
    check[y][x] = 1
    answer[y][x] = 1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if check[ny][nx]!=1:
            if test[ny][nx] < test[y][x]:
                check[ny][nx]=1








