n= int(input())
stair=[]
for i in range(n):
    stair.append(int(input()))


dp=[0 for i in range(n)]

def solvedp(n):
    dp[0] = stair[0]
    dp[1] =stair[1]+stair[0]
    dp[2] = max(dp[1],dp[0]+stair[2],stair[1]+stair[2])
    for i in range(3,n):
        dp[i] = max(dp[i-1],dp[i-2]+stair[i],stair[i-1]+stair[i])

    return dp[n-1]

ans = print(solvedp(n))

