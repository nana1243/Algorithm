# 이진트리의 최대 깊이를 구하여라

from collections import deque

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:

    def __init__(self,data):
        self.root = data

    def maxDepth(self):
        root = self.root
        if root is None:
            return 0

        queue = deque(root)
        depth = 0

        while queue:
            depth+=1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth


test=[]
t = Tree([1,2,3,None,None,9,10])

print(t.maxDepth())
