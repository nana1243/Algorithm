# 정렬되어 있는 두 연결리스트를 합쳐라




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
            self.last = node
        else:
            curr = self.head
            while curr.next!=None:
                curr = curr.next
            curr.next = node

    def display(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


    def delte(self,data):
        if self.head==None:
            return False
        if self.head.data == data:  # 지우고자 하는 노드가 맨 앞
            temp = self.head
            self.head = self.head.next
            del temp
            return True

        node = self.head
        while node.next:
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next
                del temp
                return True  # 지우고자 하는 노드를 찾아 지웠을 경우
            node = node.next

        # 지우고자 하는 노드가 없을 경우
        return False

    def MergeTwoLinkedList(self,l1:Node,l2:Node):
        if(not l1) or (l2 and l1.data >l2.data):
            l1,l2 = l2,l1

        if l1:
            l1.next = self.MergeTwoLinkedList(l1.next,l2)

        return self.display()






l1 = MyLinkedList()
l1.add(Node(1))
l1.add(Node(2))
l1.add(Node(4))

l2 = MyLinkedList()
l2.add(Node(1))
l2.add(Node(3))
l2.add(Node(4))


print(l1.MergeTwoLinkedList(l1.head,l2.head))