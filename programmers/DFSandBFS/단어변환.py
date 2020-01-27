words=["hot", "dot", "dog", "lot", "log", "cog"]
begin="hit"
target="cog"

# 글자중에 한 글자 차이 나는 것이 존재한다면 , 그것의 index로 edge 그래프를 만든다
from collections import Counter

edge = [[] for i in range(len(words)+1)]
for i in range(len(words)):
    if len(Counter(words[i]) - Counter(begin)) == 1: edge[0].append(i+1)

for i in range(len(words)):
    for j in range(len(words)):
        words[j] = words[j].lower()
        if len(Counter(words[i]) - Counter(words[j])) == 1:
            edge[i+1].append(j+1)

start=0
end=words.index(target)+1

def dfs():
    cnt = 0
    d_visit = []
    stack = [start]
    d_check = [0 for _ in range(len(edge)+1)]
    while stack:
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += edge[v1]
            cnt+=1
    return d_visit
print(dfs())

def solution(begin, target, words):
    import collections
    adj = [[] for i in range(len(words))]
    for i in range(len(words)):
        for j in range(len(words)):
            words[j] = words[j].lower()
            if len(collections.Counter(words[i]) - collections.Counter(words[j])) == 1:
                adj[i].append(j)
    print(adj)

    for i in range(len(words)):
        a = collections.Counter(begin) - collections.Counter(words[i])
        if len(a) == 1 and list(a.values())[0] == 1:
            begin = words[i]
            break

    def dfs(begin, target, words):
        if target not in words:
            return 0
        if begin not in words:
            return 0
        else:
            begin = words.index(begin)
            target = words.index(target)
            stack = [begin]
            d_visit = []
            d_check = [False for i in range(len(words))]
            while stack:
                node = stack.pop()
                if node == target:
                    d_check[node] = True
                    d_visit.append(words[target])
                    break
                if d_check[node] != True:
                    d_check[node] = True
                    d_visit.append(words[node])
                    for w in adj[node]:
                        stack.append(w)
        return len(d_visit)

    return dfs(begin, target, words)