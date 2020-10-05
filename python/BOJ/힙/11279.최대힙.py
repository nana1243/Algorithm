import heapq
import sys


n=int(sys.stdin.readline())
h=[]
heapq.heapify(h)
for i in range(n):
    n=int(sys.stdin.readline())
    if n==0:
        if len(h)==0:
            print(0)
            continue
        p=(-1)*heapq.heappop(h)
        print(p)
    else:
        push=-n
        heapq.heappush(h,push)

