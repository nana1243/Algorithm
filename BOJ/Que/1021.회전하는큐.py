
from collections import deque
n,m=map(int,input().split(" "))
que=deque()

for i in range(n):
    que.append(i+1)

print(que)
que.rotate(1)
print(que)


for i in range(m):
    idx=list(map(int,input().split(" ")))

def command():
    que.popleft()
    que.rotate(-1)
    que.rotate(1)
    return que

