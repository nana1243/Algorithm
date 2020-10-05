def solution(N):
    dp=[1,1,2,3,5,8]
    if N>=6:
        for i in range(6,N+1):
            dp.append(dp[i-1]+dp[i-2])
    answer=2*(dp[N-1]+dp[N])
    return answer