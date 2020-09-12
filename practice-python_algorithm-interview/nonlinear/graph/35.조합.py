n = 4
k = 3

# 4개중 2개를 뽑는 것
# 조합을 할땐, start를 정해줘서 앞의 숫자를 조절한다

ans=[]
def dfs(elements,start,limit):
    if limit==0:
        ans.append(elements[:])

    for i in range(start,n+1):
        elements.append(i)
        dfs(elements, i+1 , limit-1)
        elements.pop()

    return ans

dfs([],1,k)
print(ans)


