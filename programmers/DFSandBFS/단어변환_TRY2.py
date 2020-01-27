def solution(begin, target, words):
    # target의  문자가 없을 경우
    if target not in words:
        return 0

    end = words.index(target) + 1
    # edge 그래프 형성
    edge = [[] for i in range(len(words) + 1)]
    from collections import Counter
    for i in range(len(words)):
        if len(Counter(begin) - Counter(words[i])) == 1:
            edge[0].append(i + 1)

    if len(edge) == 0:
        return 0

    for i in range(len(words)):
        for j in range(len(words)):
            if len(Counter(words[i]) - Counter(words[j])) == 1:
                if j + 1 not in edge[i + 1]:
                    edge[i + 1].append(j + 1)
                if i + 1 not in edge[j + 1]:
                    edge[j + 1].append(i + 1)

    #################### edge 그래프형성 끝 ######################

    from collections import deque
    q = deque()
    check = [0 for i in range(len(words) + 1)]
    visit = []

    def bfs(start):
        layer = {start: 1}
        check[start] = 1
        q.append(start)
        while q:
            p = q.popleft()
            for e in edge[p]:
                if check[e] == 0:
                    check[e] = 1
                    layer[e] = layer[p] + 1
                    q.append(e)
        return layer[end]

    answer = []
    for i in range(len(edge[0])):
        answer.append(bfs(edge[0][i]))

    return min(answer)





