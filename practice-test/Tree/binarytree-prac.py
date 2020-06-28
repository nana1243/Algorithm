"""
이진트리는 다음과 같은 조건을 지님
1. 왼쪽 자식 노드에는 부모 노드보다 작은 값을 가진 노드가 옴
2. 오른쪽 자식 노드에는 부모 노드보다 큰 값을 가진 노드가 옴
3. 루트 노드부터 리프 노드까지 모두에게 적용됨
4. 단 리프 노드는 왼쪽, 오른쪽 자식이 NULL
5. 탐색과 , 삭제 에  용이할수 도 있으나, 균형잡힌 tree가 아닐경우 오히려 효율성이 떨어짐!
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.right= None
        self.left = None

    def __str__(self):
        return str(self.data)

class Tree:
    # 조상이 누군지 생성자를 생성할때 넣어준다
    def __init__(self,root):
        self.root = root

    def search(self,data):
        self.curr_node = self.root

        while self.curr_node:
            if self.curr_node.data == data:
                print(data)
                return True

            elif self.curr_node.data>data:
                self.curr_node = self.curr_node.left

            else:
                self.curr_node = self.curr_node.right

        return False



    def insert(self,data):
        self.curr_node = self.root

        while True:
            # 만약 현재의 node의 데이터< data
            if self.curr_node.data<data:
                if self.curr_node.right !=None:
                    self.curr_node = self.curr_node.right
                else:
                    self.curr_node.right = Node(data)
                    break

            else:
                if self.curr_node.left !=None:
                    self.curr_node = self.curr_node.left
                else:
                    self.curr_node.left = Node(data)
                    break

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        # node가 없으면(찾는 데이터가 없으면 false)
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right :
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)

        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted


    def traverse(self):
        curr= self.root
        queue = [curr]
        while queue:
            root = queue.pop(0)
            if root is not None:
                print(root.data)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return



arr = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = Tree(15)
for elm in arr:
    bst.insert(elm)


bst.traverse()









