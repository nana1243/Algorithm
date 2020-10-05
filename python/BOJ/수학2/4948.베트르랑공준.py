# n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

import math
def isPirme(x):
    if x<=1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

while True:
    n=int(input())
    answer=0
    if n==0:
        break
    for i in range(n+1,2*n+1):
        if isPirme(i)==True:
            answer+=1
    print(answer)
