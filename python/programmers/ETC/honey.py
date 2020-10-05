####### 1.10진법 -> n진법변환 ##########

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

print(convert(2,2))
print(convert(0,2))

# def change_binary(n : int) -> int:
#     result, idx = 0,0
#     while (n >=1):
#         remainder =n % 2
#         n = n // 2
#         result += (10**idx)* remainder
#         idx +=1
#     return result


##################################

####2. n진법 -> 10진법 ##########

num = '3212'
base = 5
answer = int(num, base)
print(answer)

####################################

###########3. 소수판별하기 ##########



# 소수인지 검사하는 함수(isPrime)를 만든다.
# 1부터 100 사이의 소수를 구하는 파이썬 코드이다.

n=100
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True


for i in range(n+1):
  if(isPrime(i)):
    print(i)