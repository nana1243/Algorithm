# 여러명의 사람들이 줄을 서있다
# 각각의 사람은 (h,k)의 두정수 쌍을 갖는데, h: 키, k:자신의 키 이상인 사람들의 수를 뜻한다
# 이 값이 올바르도록 줄을 재정렬 하는 알고리즘을 써라


test=[
    [7,0],[4,4],[7,1],[5,0],[6,1],[5,2]
]

# 우선순위큐를 활용

import heapq
def reconstructQue(people:list):
    heap=[]
    for person in people:
        heapq.heappush(heap, (-person[0],person[1]))

    result=[]

    while heap:
        out = heapq.heappop(heap)
        height,idx=out[0],out[1]
        result.insert(idx,[-height,idx])

    return result


print(reconstructQue(test))




