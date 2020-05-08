# 10000

s=set()
def construct_number(n):
    dn=sum(list(map(int,str(n))))+n
    if dn>10000:
        return s
    else:
        s.add(dn)
    return construct_number(dn)

for i in range(1,10001):
    if i in s:
        continue
    else:
        construct_number(i)


allset=set()
for i in range(1,10001):
    allset.add(i)
answer=sorted(allset-s)
for element in answer:
    print(element)