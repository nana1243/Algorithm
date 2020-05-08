n=int(input())
a=list(map(int,input().split(" ")))
dp=[0 for i in range(n)]


def solve(a:list):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]<a[j] and dp[i]<dp[j]:
                dp[i]=dp[j]
        dp[i] += 1
    return dp


print(solve(a))



#
# def solve(a:list):
#     answer=0
#     for i in range(len(a)):
#         compare = a[i]
#         ans = [a[i]]
#         for j in range(i + 1, len(a)):
#             compare = max(compare, a[j])
#             if compare in ans:
#                 continue
#             else:
#                 ans.append(compare)
#
#         answer=max(answer,len(ans))
#     return answer
#
# print(solve(a))
#
#
