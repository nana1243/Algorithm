### 소수이냐 판별 ####
def isPrime(n):
    if n==0 or n==1:
        return False
    import math
    m=int(math.sqrt(n))
    for i in range(2,m+1):
        if n%i==0:
            return False
    return True

numbers="17"
# return 3
numbers="011"
# return 2 11, 101,

####### step2 만들 수 있는 가지의 수를 만들어 보자 ! #####

from itertools import permutations

### 만들고 싶은 수를 리스트 형식으로 만든후 그안의 원소를 join을 하고 싶은 경우
cnt=0
permutation_set = set([int("".join(item)) for i in range(7) for item in set(permutations(list(numbers), i + 1))])

for element in permutation_set:
    if isPrime(element)==True:
        cnt+=1

print(cnt)