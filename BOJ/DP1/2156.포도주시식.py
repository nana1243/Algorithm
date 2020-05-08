n=int(input())
weight=[0 for i in range(n)]
for i in range(n):
    weight[i]=int(input())


print(weight)

def solvedp():
    dp=[0 for i in range(n)]
    if n==1:
        dp[0]=weight[0]
    elif n==2:
        dp[0] = weight[0]
        dp[1] = weight[0] + weight[1]
    else:
        dp[0] = weight[0]
        dp[1] = weight[0] + weight[1]
        dp[2] = max(weight[0] + weight[2], weight[1] + weight[2], dp[1])
        for i in range(3, len(dp)):
            dp[i] = max(dp[i - 2] + weight[i], dp[i - 3] + weight[i] + weight[i - 1], dp[i - 1])

    return dp[n-1]

print(solvedp())