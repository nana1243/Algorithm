n=int(input())
test=list(map(int,input().split(" ")))

def is_prime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

answer=0
for i in range(len(test)):
    if is_prime(test[i])==True:
        answer+=1

print(answer)