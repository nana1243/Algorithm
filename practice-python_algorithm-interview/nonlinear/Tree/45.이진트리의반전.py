class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,input_data):
        self.list = list(reversed(input_data))
        self.root = Node(input_data[-1])
        self.tree = []

    def insertNode(self):
        while self.list:
            try:
                curr = Node(self.list.pop())
                self.tree.append(curr)
                if curr.left is None:
                    curr.left = Node(self.list.pop())
                    self.tree.append(curr.left)
                if curr.right is None:
                    curr.right = Node(self.list.pop())
                    self.tree.append(curr.right)
            except IndexError:
                break

    def invertTree(self,root:Node):
        if root:
            root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
            return root
        return None




t = Tree([4,2,7,1,3,6,9])
t.insertNode()


