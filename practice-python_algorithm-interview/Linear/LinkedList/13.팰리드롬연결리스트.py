
from collections import deque
# 연결리스트가 팰린드롬 구조인지 판별하라


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    # add new node at the end of linked list
    def add(self,node:Node):
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next!=None:
                curr = curr.next
            curr.next = node


    def isPalindrome1(self):
        head = self.head
        q = deque()
        if not self.head:
            return True

        node = head
        while node is not None:
            q.append(node.data)
            node = node.next


        while len(q)>1:
            if q.popleft() != q.pop():

                return False
        return True

    def isPalidrome2(self):

        head = self.head
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev,rev.next ,slow = slow,rev,slow.next

        if fast:
            slow = slow.next

        while rev and rev.data ==slow.data:
            slow,rev = slow.next , rev.next

        return not rev









case=MyLinkedList()

case.add(Node(1))
case.add(Node(2))
print(case.isPalindrome1())
case.add(Node(2))
case.add(Node(1))
print(case.isPalindrome1())

print(case.isPalidrome2())

