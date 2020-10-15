"""
인접 행렬에서 본 그래프와 같은 모양의 그래프를 예로 들 것.
입력: 그래프의 인접 리스트
출력: 위상 정렬의 순서(같은 순서일 경우 아무거나 뽑음)
알고리즘
    1. 모든 정점의 진입 차수를 계산
    2. 진입 차수가 0인 정점을 스택에 삽입
    3. 위상 순서를 생성
"""


adj = {0: [2, 3], 1: [3, 4], 2: [3, 5], 3: [5], 4: [5], 5: []}

def reverse_adj(adj):
    reverse = {key :[] for key in adj.keys()}

    for key in adj:
        for elm in  adj[key]:
            reverse[elm].append(key)

    return reverse


def makeDegree(reverse:adj):
    d={ key : 0 for key in reverse.keys()}
    for key in reverse:
        value = len(reverse[key])
        d[key] +=value

    return d

reverse = reverse_adj(adj)
degree = makeDegree(reverse)
print(degree)

def topological_sort(degree:dict,reverse):
    stack=[]
    answer=[]

    for key in degree:
        if degree[key] == 0:
            stack.append(key)

    while stack:
        out = stack.pop()
        answer.append(out)

        for elm in adj[out]:
            degree[elm]-=1
            if degree[elm]==0:
                stack.append(elm)

    return answer




answer = topological_sort(degree,reverse)

print(answer)