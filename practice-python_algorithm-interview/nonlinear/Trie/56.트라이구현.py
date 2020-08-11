

class TrieNode:
    def __init__(self):
        self.word = False
        self.children={}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word:str):
        node = self.root

        for char in word:
            if char not in node.children:
                print(char)
                node.children[char] = TrieNode()
            node = node.children[char]

        node.word = True

    def printchildren(self):
        return self.root.children

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word==True

    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True




trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("pple")
print(trie.printchildren())
print(trie.search("app"))
print(trie.search("pp"))

