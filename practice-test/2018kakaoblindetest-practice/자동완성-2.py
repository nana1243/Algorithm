class Node:
    def __init__(self, char, data=None):
        self.char = char  # 노드의 글자
        self.data = data  # 마지막 노드일떄 string값
        self.possible_word = 0  # 해당 노드를 거쳐갈 경우 가능한 글자의 갯수
        self.children = {}

    def __str__(self, data):
        return str(self.data)


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        # 1. 가장 앞단의 self.head를 현재지점으로 설정해준다
        # 2. 그리고 넣고자 하는 string을 넣어준다
        # 2-1 이미넣어져있는 단어가 존재한다면 pass
        # 2-1 그렇지 않다면 해당 데이터를 넣어준다
        # 2-1 넣어져 있다면 pass를 하는 대신, 현재의 지점은 update를 지속적으로 해주어야함
        #### ex> gone 리면, currnode = g -> 존재 -> currnode = currnode.children[char]의 형태로 currr을 지속적을 update해준다
        # 3. for문이 끝나면, 항상 마지막char에 넣을 수 있는 공간이 +1이라고 지정해준다
        # 4. 또한 마지막 분기점에 해당 데이터 완전체를 삽입하게 한다
        currnode = self.head
        for char in string:
            currnode.possible_word += 1
            if char not in currnode.children:
                currnode.children[char] = Node(char)
            currnode = currnode.children[char]
        currnode.possible_word += 1
        currnode.data = string

    def search(self, string):
        # 1.가장 앞쪽에서 시작한다
        # 2. 찾고자하는 string의 char을 순차적으로 찾기 시작한다
        # 3-1. 해당 char이 currnode.children으로 존재할때까지 cur을 update해준다
        # 3-2. 만약 하나라도 다르다면, return False가 나온다
        # 4. 그리고 마지막 글자의 possible=1이라면 해당 문자가 존재하는 것이고
        # 4-1 그렇지 않다면, 해당문자는 존재하지 않고, 그 부분만 존재하는 것이다
        currnode = self.head
        for char in string:
            if char in currnode.children:
                currnode = currnode.children[char]
            else:
                return False
        # 해당 노드까지 왔을 때 만들 수 있는 문자의 개수가 1이면 True 반환
        if currnode.possible_word == 1:
            return True
        else:
            return False


def solution(words):
    cnt = 0
    word_trie = Trie()
    ### trie를 생성하고,트라이라는 구조안에 word을 넣자
    for word in words:
        word_trie.insert(word)

    ## 이제 그 문자가 존재하는지를 찾고 존재할당시 몇개의 단어만 쳐도
    ## 되는지 찾아보자

    for word in words:
        # 초기값을 false라고 해두자
        already_find = False

        for i in range(1, len(word) + 1):
            if word_trie.search(word[:i]):
                cnt += len(word[:i])
                already_find = True
                break
        if not already_find:
            cnt += len(word)
    return cnt

