n=int(input())
m=int(input())
def isPrime(x):
    if x<=1:
        return False
    else:
        for i in range(2, x):
            if x%i==0:
                return False
    return True

answer1=[]
for i in range(n,m+1):
    if isPrime(i)==True:
        answer1.append(i)

print(answer1)
if len(answer1)==0:
    print(-1)
else:
    print(sum(answer1))
    print(answer1[0])

