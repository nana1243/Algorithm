from collections import deque
class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self,rootdata):
        self.root = TreeNode(rootdata)

    def maxDepth(self,testacase):
        root = self.root
        que=deque([root])
        depth=1

        while que and testcase:
            depth+=1
            for _ in range(len(que)):
                curr_root = que.popleft()

                if curr_root.left is None :
                    curr_root.left =TreeNode(testacase.pop(0))
                    que.append(curr_root.left)

                if curr_root.right is None:
                    curr_root.right = TreeNode(testacase.pop(0))
                    que.append(curr_root.right)


        return depth


testcase=[3,9,20,None,None,15,7]

bst = BinaryTree(testcase.pop(0))
depth=bst.maxDepth(testcase)
print(depth)