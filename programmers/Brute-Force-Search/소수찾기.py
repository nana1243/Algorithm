def solution(numbers):
    import math
    def isPrime(num):
        if num == 1 or num==0: return False
        n = int(math.sqrt(num))
        for k in range(2, n+1):
            if num % k == 0:
                return False
        return True
    
    from itertools import permutations
    def sol(numbers):
        permutation_set = \
        set([int("".join(item)) for i in range(7) for item in set(permutations(list(numbers), i + 1))])
        return permutation_set
    cnt=0
    permution_set=sol(numbers)
    for element in  permution_set:
        if isPrime(element)==True:
            cnt+=1
    return cnt