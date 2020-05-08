cities=int(input())
parent=[i for i in range(len(cities))]
m=int(input())


# 부모노드를 찾는 것
def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]


def union(x,y):
    rootx=find(x)
    rooty=find(y)
    if rootx !=rooty:
        parent[rooty]=rootx



