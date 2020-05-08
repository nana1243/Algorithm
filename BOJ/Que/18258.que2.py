
from collections import deque
import sys
q=deque()
n=int(sys.stdin.readline())


def command(c):
    if c[0]=="push":
        q.append(int(c[1]))

    elif c[0]=="front":
        if len(q)==0:
            return -1
        else:
            return q[0]

    elif c[0]=="back":
        if len(q)==0:
            return -1
        else:
            return q[-1]

    elif c[0] == "pop":
        if len(q) == 0:
            return -1
        else:
            return q.popleft()

    elif c[0] == "size":
        return len(q)

    elif c[0] == "empty":
        if len(q) == 0:
            return 0
        else:
            return -1


for i in range(n):
    s=sys.stdin.readline().split(" ")
    s[0]=s[0].strip()

    if s[0]=="push":
        q.append(int(s[1]))

    elif s[0]=="front":
        if len(q)==0:
            print(-1)
        else:
            print(s[0])

    elif s[0]=="back":
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])

    elif s[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    elif s[0] == "size":
        print(len(q))

    elif s[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(-1)


