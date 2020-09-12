from collections import deque

testcase=[1,2,3,4,5]

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    longest: int = 0

    def __init__(self,testcase):
        self.root =None
        self.testcase= testcase

    def dfs(self,node,long):
        if not node.left or node.right:
            return -1
        leftlong = self.dfs(node.left, long+1)
        rightlong = self.dfs(node.right,long+1)

        return leftlong + rightlong

    def insert(self):
        testcase = deque(self.testcase)
        ans=[]
        while testcase:
            for _ in range(len(testcase)):
                try:
                    curr = TreeNode(testcase.popleft())
                    ans.append(curr.data)
                    if curr.left is None:
                        curr.left = TreeNode(testcase.popleft())
                        ans.append(curr.left.data)
                    if curr.right is None:
                        curr.right = TreeNode(testcase.popleft())
                        ans.append(curr.right.data)
                        break
                except IndexError:
                    break
        return ans

    def solution(self):
        self.insert()
        ans=self.dfs(self.root,0)
        return ans





t = Tree(testcase)
ans=t.solution()
print(ans)
