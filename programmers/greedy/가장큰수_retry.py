from collections import deque

number="1924"
q=deque(number)
k=2
answer =""
long=len(number)-k
# 첫번쨰 과정

def recursion(k,q):
    first=0
    input=max(number[first:k+1])
    for i in range(q.index(input)):
        k-=1
        q.popleft()
    if len(q)==long:
        answer="".join(q)
        return answer
    return recursion(q,k)
print(recursion(k,q))