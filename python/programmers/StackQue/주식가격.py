def solution(prices):
    
    def f(n):
        cnt=0
        for i in range(n+1, len(prices)):
            if prices[n]>prices[i]:
                cnt+=1
                break
            else:
                cnt+=1
        return cnt
                
    answer=[]
    for i in range(0,len(prices)-1):
        result=f(i)
        answer.append(result)
    answer.append(0)
    return answer