
n=int(input())

for i in range(n):
    line=list(input())
    ans = 0
    cnt=0
    for j in range(len(line)):
        if line[j]=="O":
            ans+=1
            cnt+=ans
        else:
            ans=0
    print(cnt)
