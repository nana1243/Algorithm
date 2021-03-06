
# n=int(input())

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

class Stack():
    def __init__(self):
        self.items=[]
    def size(self):
        print(len(self.items))

    def push(self, data):
        self.items.append(data)


    def pop(self):
        if len(self.items)==0:
            print(-1)
        else:
            last_data=self.items.pop()
            print(last_data)

    def top(self):
        if len(self.items)==0:
            print(-1)
        else:
            print(self.items[-1])

    def empty(self):
        if len(self.items)==0:
            print(1)
        else:
            print(0)

import sys

n=sys.stdin.readline().strip()
n=int(n)

s=Stack()
for i in range(n):
    todoit=sys.stdin.readline().strip()
    if todoit[0]=="push":
        s.push(todoit[1])
    elif todoit[0]=="empty":
        s.empty()
    elif todoit[0]=="pop":
        s.pop()
    elif todoit[0]=="top":
        s.top()
    elif todoit[0]=="size":
        s.size()

