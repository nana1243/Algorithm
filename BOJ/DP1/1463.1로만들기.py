import sys


n = int(sys.stdin.readline())

dp= [[]for i in range(n)]

def solvedp(n):
    if n%3==0:
        dp[0].append(n//3)
    if n%2 ==0:
        dp[0].append(n//2)
    if n-1>0:
        dp[0].append(n-1)
    if 1 in dp[0]:
        return 1
    for i in range(1,n):
        for j in range(len(dp[i-1])):
            if dp[i-1][j] % 3 == 0:
                dp[i].append(dp[i-1][j] //3)
            if dp[i-1][j] % 2 == 0:
                dp[i].append(dp[i-1][j] //2)
            if dp[i-1][j] -1 >0:
                dp[i].append(dp[i-1][j] -1)
        if 1 in dp[i]:
            return i+1



print(solvedp(n))