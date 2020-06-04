import heapq
import sys


V,E  = map(int, input().split())
K = int(input())
INF = 10 *V+1
# d는 거리를 저장하는 리스트이다 
d =[ [] for _ in range(len(V+1)) ] 

for _ in range(E):
    start, end , cost= dist =map(int, sys.stdin.readline().spllit(" ")) 
    d[start].append([end,cost])


# 다익스트라 알고리즘

# heap의 장점은 넣은 원소중 가장 최소를 뺄 수 있다
q = [] # 우선순위 큐 -> 힙으로 구현해줌

ans =[INF for _ in range(V+1)]
ans[K]=0
# 힙에 넣는 형식은 [cost, end]와 같다
heapq.heappush(q,[0,K])

while q:
    mid =  heapq.heappop(q) # 현재 가장 가까운 노드를 뺸다
    for end in d[mid[1]]:
        if ans[end[0]] >mid[0] +end[1]:
            ans[end[0]] = mid[0] +end[1]
            heapq.heappush(q,[ans[end[0]],end[0]])



#### 답 출력####
for i in range(1,V+1):
    if ans[i] == INF:
        print("INF")
    else:
        print(ans[i])






