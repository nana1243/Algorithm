t= int(input())

testcase=[]
ans=[(1,0),(0,1),(1,1)]

for i in range(t):
    put=int(input())
    testcase.append(put)





for j in range(2,testcase[i]+1):
    z=ans[j-1][0]+ans[j-2][0]
    o=ans[j-1][1]+ans[j-2][1]
    ans.append((z,o))