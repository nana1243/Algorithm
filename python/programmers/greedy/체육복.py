def solution(n, lost, reserve):
    #lost ->0,reserve->2
    total=[1 for i in range(n)]
    for l in lost:
        total[l-1]-=1
    for r in reserve:
        total[r-1]+=1
    # 옆에 여별이 있다면 여벌을 빌리자
    # 이때 양끝을 고려한 것과 고려하지 않은 것으로 크게 나누고
    # 그리고 거기서 0이라면 고려해보자
    
    for i in range(n):
        if i==0:
            if total[i]<=0 and total[i+1]>=2:
                total[i]+=1
                total[i+1]-=1
        if 0<i<n-1:
            if total[i]<=0:
                if total[i-1]>=2:
                    total[i-1]-=1
                    total[i]+=1
                if total[i+1]>=2:
                    total[i+1]-=1
                    total[i]+=1

        if i==n-1:
            if total[i]<=0 and total[i-1]>=2:
                total[i]=1
                total[i-1]=1
        
    for i in range(n):
        if total[i]>=2:
            total[i]=1
    return sum(total)