import sys
from heapq import heappop
from heapq import heappush

v,e = map(int,input().split(" "))
start = int(input())
graph=[[] for _ in range(v+1)] # 주어진 그래프 생성할 리스트



############# 그래프 생성하기  start ############
for i in range(e):
    s,e,c = map(int,input().split(" "))
    graph[s].append([c,e])
############# 그래프 생성하기  end ############


INF = sys.maxsize

# 답이 될 리스트 (각 start-> target으로 갈때 최소비용을 저장한다)
dis =[ INF for _ in range(v+1)]
dis[start]=0

que=[]
heappush(que, [0,start]) # start의 끝점은 start이고 , 거기의 cost =0 으로 설정

while que:
    mid = heappop(que)
    for end in graph[mid[1]]:
        if dis[end[1]]> mid[0]+end[0]:
            dis[end[1]] = mid[0]+end[0]
            heappush(que, [dis[end[1]], end[1]])




