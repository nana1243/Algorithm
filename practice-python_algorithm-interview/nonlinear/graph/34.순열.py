
# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하여라

test=[1,2,3]
prev_elements=[]

ans=[]

def dfs(elements:list):
    if len(elements)==0:
        ans.append(prev_elements[:])
        return 

    for e in elements:
        next_elemnts=elements[:]
        next_elemnts.remove(e)

        prev_elements.append(e)
        dfs(next_elemnts)
        prev_elements.pop()


dfs(test)
print(ans)
