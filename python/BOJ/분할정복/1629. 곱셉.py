from math import pow

n,m,k = map(int,input().split(" "))

def solve(a,b,c):
    answer  = pow(a,b,mod=c)
    return answer

answer = solve(n,m,k)
print(answer)