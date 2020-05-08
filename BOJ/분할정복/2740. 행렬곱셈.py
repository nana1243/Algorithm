n,m=map(int,input().split(" "))
A=[]

for i in range(n):
    A.append(list(map(int,input().split(" "))))


m,k= map(int,input().split(" "))

B=[]

for i in range(m):
    B.append(list(map(int,input().split(" "))))


ans=[[0 for j in range(k)]for i in range(n)]

for i in range(n):
    for j in range(k):
        for u in range(m):
            ans[i][j] += A[i][u] * B[u][j]


for i in range(n):
    for j in range(k):
        print(ans[i][j],end=" ")
    print()
