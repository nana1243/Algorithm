N,K= map(int,input().split(" "))

testcase=[0 for i in range(N)]
for i in range(N):
    weight,cost=map(int,input().split(" "))
    testcase[i]=(weight,cost)



def solvedp():
    dp=[[0,0] for i in range(N)]
    answer=0
    for j in range(len(dp)):
        if testcase[j][0]>K:
            continue
        dp[j][0]=testcase[j][0]
        dp[j][1]=testcase[j][1]
        for i in range(j+1,len(testcase)):
            if testcase[i][0]+dp[j][0]>K:
                continue
            dp[j][0]+=testcase[i][0]
            dp[j][1]+=testcase[i][1]
        answer=max(answer,dp[j][1])
    return answer

print(solvedp())