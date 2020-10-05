n,m=map(int,input().split(" "))

parent=[i for i in range(n+1)]


def find(c):
    if parent[c]==c: return c
    parent[c]=find(parent[c])
    print(parent)
    return parent[c]



def union(a,b):
    rootA=find(a)
    rootB=find(b)
    if not rootA==rootB:
        parent[rootB]=a


for i in range(m):
    command,group1,group2=map(int,input().split(" "))
    if command==0:
        union(group1,group2)
        continue
    if command==1:
        root1=find(group1)
        root2=find(group2)
        if root1==root2:
            print("YES")
        else:
            print("NO")

