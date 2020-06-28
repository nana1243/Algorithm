class Node:
    def __init__(self,key,data=None):
        self.key =key
        self.data = data
        self.children = {}

class Trie():
    # 가장 초기에 만들어지는 조건 (아무런 데이터가 없는 뼈대만 있는 형태)
    def __init__(self):
        self.head = Node(None)
    def insert(self,string):
        curr=self.head

        for char in string:
            if char not in curr.children:
                curr.children[char]=Node(char)

            curr=curr.children[char]
        curr.data=string


    def search(self,string):
        curr = self.head

        for char in string:
            if char in curr.children:
                curr= curr.children[char]
            else:
                False

        if (curr.data != None):
            return True




words=["go","gone","guild"]

trie = Trie()


for word in words:
    trie.insert(word)

print(trie.search("gone"))

""" 주어진 prefix 로 시작하는 단어들을 트라이에서 찾아 리스트 형태로 반환합니다. """


# def startwith(self, prefix):
#     curr = self.head
#     result = []
#     subtrie = None
#
#     # 트라이에서 prefix 를 찾고, # prefix의 마지막 글자 노드를 subtrie로 설정
#
#     for char in prefix:
#         if char in curr.children[char]:
#             curr = curr.children[char]
#             subtrie = curr
#         else:
#             return False
#     # bfs 로 prefix subtrie를 순회하며 # data가 있는 노드들(=완전한 단어)를 찾는다.
#
#     que = list(subtrie.children.values())
#     print(que)
#
#     while que:
#         curr = que.pop()
#         if curr.data != None:
#             result.append(curr.data)
#         que += list(curr.children.values())
#
#     return result
