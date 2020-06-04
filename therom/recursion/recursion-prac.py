
import sys
sys.getrecursionlimit(10000) # 함수호출에서 너무 많이 호출하면 런타임에러가 난다 이를 방지하기 위한 코드



######################## 하노이의 문제풀이###########################
# n개의 원판이 있다고 가정하자
# 그렇다면 n-1개의 원판은 2번째로 옮겨야 하며 , 1개의 원판은 3번째 링으로 옮긴다
# 그러고 나서 n-1개의 원판을 3번째 링으로 옮긴다
# n개의 원판을 1->3으로 옮기자
### 이를 수식으로 옮기면?
### hanoi (1) = move(1,start, tmp,target)
### hanoid(n-1) = move(n-1, start, target, tmp) +
#                 move( 1, start, tmp,target) +
#                 move( n-1, tmp,start,target)


def hanoi(n,start,tmp,end):
    if n==1:
        print(start,"->",end)
    else:
        hanoi(n-1,start,end,tmp)
        hanoi(1, start,tmp,end)
        hanoi(n-1, tmp,start,end)

hanoi(int(input()),1,2,3)

################# factorial #########################
## factorial(1) = 1 마지막 탈출조건
## factorial(n) = (n-1)*factorial(n-1)
def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

fnumber = factorial(5)
print(fnumber)



#####################pibonachi##################

def pibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return pibo(n-1)+pibo(n-2)
pibonumber = pibo(10)
print(pibonumber)

def pibo2(n):
    a = [0,1,1,2]
    if n<=len(a)-1:
        return a[n-1]

    for i in range(4,n):
        result = a[i-1]+a[i-2]
        a.append(result)
    return a[n-1]
