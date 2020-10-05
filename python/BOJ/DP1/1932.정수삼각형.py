n=int(input())
dp=[[] for i in range(n)]

for i in range(n):
    line=list(map(int,input().split(" ")))
    dp[i]=line


def solvedp():
    dp[1][0] = dp[0][0]+dp[1][0]
    dp[1][1] = dp[0][0]+dp[1][1]
    for i in range(2,n):
        for j in range(n):
            if j==0:
                dp[i][0] += dp[i-1][0]
            elif j==n-1:
                dp[i][n-1] += dp[i-1][n-1]
            else:
                dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])
    return max(dp[n-1])
ans = solvedp()
print(ans)

