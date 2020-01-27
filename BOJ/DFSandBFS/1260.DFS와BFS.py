# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.




# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.


############ coding start #######################

# 가장 먼저 입력을 한다

import sys
N, M, V = map(int, sys.stdin.readline().strip().split())
edge = [[] for _ in range(N+1)]

# 양방향이기 때문에
for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    edge[n1].append(n2)
    edge[n2].append(n1)

print(edge)
for e in edge:
    e.sort(reverse=True)



def dfs():
    danswer=[]  # 지나간 순서를 담을 리스트
    dcheck=[0 for i in range(N+1)] # 갔는지 체크 하는 리스트
    stack=[V]
    while stack:
        a=stack.pop()
        if dcheck[a]!=1:
            dcheck[a]=1
            danswer.append(a)
            stack+=edge[a]
    return danswer

print(dfs())


def bfs():
    banswer=[]
    bcheck=[0 for i in range(N+1)]
    q=[V]
    bcheck[V] = 1
    while q:
        a=q.pop()
        banswer.append(a)
        for i in reversed(edge[a]):
            if not bcheck[i]:
                bcheck[i] = 1
                q = [i] + q
    return banswer

print(bfs())