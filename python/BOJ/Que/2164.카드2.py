from collections import deque
import sys
num = int(sys.stdin.readline())
que=deque()

for i in range(num, 0, -1):
    que.append(i)

def greedy(q:deque):
    while len(q)>1:
        q.pop()
        q.rotate(1)
    return q[0]


print(greedy(que))