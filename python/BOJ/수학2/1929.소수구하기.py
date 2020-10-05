n,m=map(int,input().split(" "))

def solution(x,y):
    a = [False, False] + [True] * (y - 1)
    primes=[]
    for i in range(2, y+1):
        if a[i] and i>=x:
            primes.append(i)
            for j in range(2 * i, y + 1, i):
                a[j] = False

    return primes

answer=solution(n,m)

for i in range(0,len(answer)):
    print(answer[i])