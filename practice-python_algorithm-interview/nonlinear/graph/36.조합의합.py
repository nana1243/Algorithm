# 조합의 응용

candidates=[2,3,6,7]
target=7
ans=[]
def dfs(csum,start,path:list):
    if csum > target:
        return

    if csum == target:
        ans.append(path)
        return


    for i in range(start,len(candidates)):
        dfs(csum+candidates[i],i,path+[candidates[i]] )
    return ans


dfs(0,0,[])
print(ans)








