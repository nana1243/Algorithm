class TreeNode:

    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None

class Tree:
    longest :int = 0
    def __init__(self):
        self.root = None

    def diameterOfBinaryTree(self):
        def dfs(node):
            if not node: # 노드가 없으면 멈춘다
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2)
            return max(left,right) +1

        dfs(self.root)
        return self.longest


