import sys

n= int(sys.stdin.readline())
m= int(sys.stdin.readline())
INF=sys.maxsize

c=[[INF for _ in range(n)] for _ in range(n)]

for i in range(m):
    s,e,cost = map(int,sys.stdin.readline().split(" "))
    c[s-1][e-1]=min(c[s-1][e-1],cost)


for mid in range(n):
    for start in range(n):
        for end in range(n):
            if start != end :
                c[start][end] =  min(c[start][end],c[start][mid]+c[mid][end])
            elif start==end:
                c[start][end]=0

for i in range(n):
    for j in range(n):
        print(c[i][j],end=" ")
    print()
