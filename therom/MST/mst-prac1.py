# 하나의 cycle이 형성되는지를 check한다

# p는 각 idx에 해당하는 자신의 부모를 저장한다
p=[]
n=4
for i in range(n):
        p.append(i)

# u의 부모를 출력
# u와 p[u]가 다를때는 p[u]에 해당되는 부모를 계속 찾아간다 그리고 마지막 u= p[u] 최종 부모를출력
def find(u):
    if u!=p[u]:
        p[u] = find(p[u])
    return p[u]


# v를 u에 영입시킨다
def union(u,v):
    # 같은 사이클 내일때 (같은 부모를 공유할때)

    root1 = find(u)
    root2 = find(v)
    p[root2] =root1


# 이제는 문제의 조건을 만족하는 최소비용 + cycle을 풀어보자

costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# 비용이 큰 내림차순으로 정렬한다

costs.sort(key = lambda x:-x[2])

mst=[]
mst_cost=0
tree_edge=0

while True:
    if tree_edge==n-1:
        break
    u,v,wt =costs.pop()
    if find(u)!=find(v):
        union(u,v)
        mst.append((u,v))
        mst_cost+=wt
        tree_edge += 1

print(mst_cost)