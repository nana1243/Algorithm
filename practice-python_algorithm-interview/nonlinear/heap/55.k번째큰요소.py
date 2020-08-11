# 정렬되지 않은 배열에서 k 번째 가장 큰요소를 추출

import heapq

test=[3,2,3,1,2,4,5,5,6]
k = 4


def sol1(test:list,k):
    h=[]
    for elm in test:
        heapq.heappush(h,-elm)
    answer=[]
    for idx in range(k):
        out = heapq.heappop(h)
        answer.append(-out)

    return answer[-1]


print(sol1(test,k))


def sol2(test:list,k):
    test = list(map(lambda x:-x, test))

    heapq.heapify(test)

    for _ in range(k-1):
        heapq.heappop(test)

    return -heapq.heappop(test)

print(sol2(test,k))

# heapq.nlargest
def sol3(test:list,k):
    return heapq.nlargest(k,test)[-1]

print(sol3(test,k))


def sol4(test:list,k):
    test.sort(reverse=True)
    return test[k-1]

print(sol4(test,k))