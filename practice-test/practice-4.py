import sys

#2차원

n = int(input())
read = lambda : sys.stdin.readline().strip()
matrix = [list(map(int, list(read()))) for _ in range(n)]


def dfs(matrix,cnt,x,y):
    matrix[x][y]=0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if matrix[x][y]==1:
                cnt=dfs(matrix,cnt+1,nx,ny)
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            ans.append(dfs(matrix, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)