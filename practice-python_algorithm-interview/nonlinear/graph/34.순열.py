# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하여라

test=[1,2,3]

results=[]
prev_elements=[]

def dfs(elements:list):
    if len(elements)==0:
        results.append(prev_elements[:])

    for elm in elements:
        next_element = elements[:]
        next_element.remove(elm)
        print(next_element)

        prev_elements.append(elm)

        dfs(next_element)
        prev_elements.pop()


dfs(test)
print(results)

from itertools import permutations

def solvebyItertools(test):
    p = list(permutations(test,len(test)))
    return p


print(solvebyItertools(test))
