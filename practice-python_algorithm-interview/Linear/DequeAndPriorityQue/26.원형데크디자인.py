

class Node:
    def __init__(self,item):
        self.item = item


class MyCircularDeque:

    def __init__(self,k:int):
        self.head ,self.tail = Node(None),Node(None)
        self.k ,self.len = k,0
        self.head.right , self.tail.left = self.tail, self.head


    def _add(self,node:Node,new:Node):
        pass


    def insertFront(self,data):
        if self.len ==self.k: # 다 찾을때
            return False

        self.len+=1
