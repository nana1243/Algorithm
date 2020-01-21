# stack 구현 예시1 (python list 사용)

class stack(list):
    def push(self,object):
        return self.append(object)

    def is_empty(self):
        if not self :
            return True
        else:
            return False

    def peek(self):
        return self[-1]

    def print(self):
        return self



s=stack()
s.push(1)
s.push(2)
print(s)

# 가장 마지막것 부터 빠진다
while s:
    data=s.pop()
    print(data, end=' ')



# stack 구현 예시2 (node 사용)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node







