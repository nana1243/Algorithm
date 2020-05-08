
n=int(input())
s=[]
for i in range(n):
    element=int(input())
    if element==0:
        if len(s)==0:
            continue
        s.pop()
    else:
        s.append(element)

print(sum(s))