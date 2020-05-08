##### 부정방정식을 풀어야 한다


n=int(input())
def solvebf(n):
    ans=n
    for i in range(1,n+1):
        if n-sum(list(map(int,str(i))))==i:
            ans=min(ans,i)
    if ans==n:
        return 0
    return ans

print(solvebf(n))

# def solvebf(n):
#     ans=""
#     k = int(math.log10(n) + 1)
#     while k -2>=0:
#         num = "1" + "0" * (k - 2) + "1"
#         a=n//int(num)
#         ans+=str(a)
#         n-=a*int(num)
#         k-=1
#     print(ans)
#     if k==1 and n%2==0:
#         ans+=str(n//2)
#     else:
#         return 0
#     return ans
#
#
# if 1<=n<10:
#     print(n)
# else:
#     print(solvebf(n))
#







