# que를 이용하여 stack구현

from collections import deque
class Mystack:
    def __init__(self):
        self.q = deque()

    def push(self,item):
        self.q.append(item)
        # 요소 삽입후 맨앞에 두는 상태로 재정렬

        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.popleft() # 재정렬된 상태이니깐

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) ==0

