weight=[3, 1, 6, 2, 7, 30, 1]
m=max(weight)
visit=[False for i in range(m+1)]
from itertools import combinations
visit[0]=True

for i in range(len(weight)):
    c=list(combinations(weight,i))
    for j in range(len(c)):
        s=sum(c[j])
        if s<=m:
            visit[s]=True
#
for idx in range(len(visit)):
    if visit[idx]==False:
        print(idx)
        break