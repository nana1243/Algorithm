import heapq

v,e = map(int,input().split(" "))
start = int(input())
graph=[[]for _ in range(v+1)]
for i in range(e):
    s,end ,cost = map(int,input().split(" "))
    graph[s].append([end,cost])


# 답이 될 리스트
distance=[ 100000 for i in range(v+1)]
distance[start]=0


#다익스트라 알고리즘
queue = [] #우선순위 큐 -> 힙으로 구현해줌

heapq.heappush(queue, [0, start]) #자기 자신으로부터 우선순위 큐를 시작한다


while queue:
    mid = heapq.heappop(queue)
    for end in graph[mid[1]]: # graph에서 연결된 모든 end점을 꺼낸다
        if distance[end[0]] > mid[0]+ end[1]: # 이때 체크해줘야한다 뭐를 ? -> 거쳐서 가는게 빠른지 아니면 direct로 가는게 빠른지
            # 그렇기 때문에 distance[target]> mid[0](가고자 하는데의 cost)+end[1]
            distance[end[0]] = mid[0] + end[1]
            heapq.heappush(queue,[distance[end[0]],end[0]])

