#### 풀이는 아래와 같고 문제조건에 맞춰서  다시해야함(귀찮아서)

# testnumber=int(input())
X,Y,T=10,8,17
# N은 가로길이 , M은 세로길이
import pprint
matrix=[[0 for _ in range(X)] for i in range(Y)]

for i in range(T):
    a,b=map(int,input().split())
    matrix[b][a]=1

cnt=0
def dfs(x,y,matrix):
    matrix[y][x]=0
    dx = [1, -1, 0, 0]
    dy = [0, -0, 1, -1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<X and ny>=0 and ny<Y:
            if matrix[ny][nx]==1:
                dfs(nx,ny,matrix)
    return

cnt=0
for i in range(X):
    for j in range(Y):
        if matrix[j][i]==1:
            dfs(i,j,matrix)
            cnt+=1
print(cnt)

# pprint.pprint(matrix)






