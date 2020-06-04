def convert(n,base):
    T="0123456789ABCDEF"
    q,r = divmod(n,base)
    n = T[r]
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

tmp1 = convert(100,2)
print(tmp1)
tmp2 = convert(4,2)
print(tmp2)


################## 소수 구하는 방법 ###################3
import math

def isPrime(n):
    if n<=1:
        return False
    s =math.sqrt(n)
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True

################## 최대공약수 구하는 법 #############

print(math.gcd(100,40))

################ 최대 공배수 구하는 법 #########

def make(n,m):
    q=math.gcd(n,m)
    ans = q*(n//q)*(m//q)
    return ans

lcd1 = make(4,14)
print(lcd1) 

############################################################