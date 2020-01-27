M=7
import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

matrix = [list(map(int, list(read()))) for _ in range(n)]


def dfs(matrix, cnt, x,y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 하고 0으로 바꾸는것 이다.
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if n_x>=0 and n_x<n and n_y>=0 and n_y<n:
            if matrix[n_x][n_y]==1:
                cnt = dfs(matrix, cnt+1, n_x, n_y)
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            ans.append(dfs(matrix, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)

