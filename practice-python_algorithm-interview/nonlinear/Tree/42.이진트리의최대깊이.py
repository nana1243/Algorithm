# 이진트리의 최대 깊이를 구하여라
from collections import deque

testcase = [3, 9, 20, None, None, 15, 7]


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self):
        self.root = None

    def insertList(self, testcase: list):
        testcase=deque(testcase)

        depth =0
        while testcase:
            depth+=1
            for _ in range(len(testcase)):
                try:
                    curr = TreeNode(testcase.popleft())
                    if curr.left is None:
                        curr.left = TreeNode(testcase.popleft())
                    if curr.right is None:
                        curr.right = TreeNode(testcase.popleft())
                        break
                except IndexError:
                    return depth

        return depth


t = Tree()
d =t.insertList(testcase)
print(d)