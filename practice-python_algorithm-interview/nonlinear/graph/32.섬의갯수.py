# 1을 육지로 ,0을 물로 => 섬의갯수는?

testcase=[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,1]]


class Solution:
    def __init__(self,testcase):
        self.testcaase=testcase
        self.ans=[]

    # recursion으로 풀이한 방법
    def dfs(self,start,end):
        if (start<0 or end>=len(testcase[0]) or start>=len(testcase) or end<0) or testcase[start][end]!=1:
            return
        testcase[start][end]=0
        self.dfs(start+1,end)
        self.dfs(start-1,end)
        self.dfs(start,end+1)
        self.dfs(start,end-1)


    def sol1(self):
        count=0
        for i in range(len(testcase)):
            for j in range(len(testcase[i])):
                if testcase[i][j]==1:
                    self.dfs(i,j)
                    print(testcase)
                    count+=1


        return count


S =Solution(testcase)
print(S.sol1())
