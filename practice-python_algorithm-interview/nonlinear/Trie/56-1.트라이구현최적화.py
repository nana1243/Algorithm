# children ={}을  defaultdict로 구현한다면 매번 if 로 체크하는
# 구문을 없앨 수 있다


from collections import defaultdict

class TireNode:
    def __init__(self):
        self.word=False
        self.children=defaultdict(TireNode)


class Trie:
    def __init__(self):
        self.root = TireNode()


    def insert(self,word:str):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self,word:str):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word == True

    def startsWith(self,prefix:str):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return  True


    def printchildren(self):
        return self.root.children


t = Trie()
t.insert("banana")
t.insert("tomato")
print(t.search("banana"))
print(t.search("banan"))
print(t.startsWith("a"))
print(t.startsWith("bana"))