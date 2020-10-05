from itertools import combinations
n,k=map(int,input().split(" "))
card = list(map(int,input().split(" ")))

a=[]

ans=list(combinations(card,3))
for j in range(len(ans)):
    if sum(ans[j])<=k:
        a.append(sum(ans[j]))
print(max(a))