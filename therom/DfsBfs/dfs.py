
edge=[[0],[2,3,4],[1,4],[1,4],[2,3,4]]
for e in edge:
    e.sort(reverse=True)
V=1
N=4
M=5
print(edge)

def dfs():
    d_visit = []
    stack = [V]
    d_check = [0 for _ in range(N+1)]
    while stack:
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += edge[v1]
    return d_visit

print(dfs())