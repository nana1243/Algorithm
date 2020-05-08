import sys
import heapq
## 1. graph 을 만들자

# V,E= map(int,input().split(" "))
# graph=[[]for i in range(V+1)]
#
# for i in range(E):
#     s,e,d=sys.stdin.readline().split(" ")
#     graph[int(s)].append((int(e),int(d)))

## 2. 다익스트라 함수를 통해 최소거리 구하기
## init을 설정한다

##que의 원소형태 (end, weight)
# def daikstra(graph:list,start):
#     que=[]
#     heapq.heappush(que,[])
#



s="hiIamHennie"
cnt=0
for i in range(len(s)):
    if s[i].isupper():
        cnt+=1

print(cnt+1)