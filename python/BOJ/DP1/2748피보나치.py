# 단순재귀로 푸는 법(python은 시간초과뜸)
n = int(input())
# def recur(n):
#     if n<=2:
#         return 1
#     else:
#         return recur(n-1)+recur(n-2)
# answer = recur(n)
# print(answer)

### 2번째 방법

def rec2(n):
    s = [0,1,1]
    if n<=2:
        return s[n]
    else:
        for i in range(3,n+1):
            put= s[i-1]+s[i-2]
            s.append(put)
    return s[n]

ans2=rec2(n)

print(ans2)