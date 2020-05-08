from collections import deque
import sys
q=deque()

def command(c):
    if c[0]=="push_front":
        q.appendleft(int(c[1]))

    elif c[0]=="push_back":
        q.append(int(c[1]))

    elif c[0]=="pop_front":
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())

    elif c[0]=="pop_back":
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())

    elif c[0]=="size":
        print(len(q))

    elif c[0]=="empty":
        if len(q)==0:
            print(1)
        else:
            print(0)

    elif c[0]=="front":
        if len(q)==0:
            print(-1)
        else:
            print(q[0])

    elif c[0]=="back":
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])

n=int(sys.stdin.readline())
for i in range(n):
    c=sys.stdin.readline().split(" ")
    c[0]=c[0].strip()
    command(c)

