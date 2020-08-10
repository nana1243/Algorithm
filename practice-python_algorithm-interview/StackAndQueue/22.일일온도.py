

testcase=[73,74,75,71,69,72,76,73]

# 부르트 포스
def sol1(testcase):
    ans=[]
    for i in range(len(testcase)-1):
        cnt=0
        for u in range(i+1,len(testcase)):
            if testcase[i]<testcase[u]:
                cnt+=1
                ans.append(cnt)
                break
            else:
                cnt+=1

    ans.append(0)
    return ans

# stack을 이용한 풀이

def sol2(testcase):
    answer = [0]*len(testcase)
    stack = []
    for i, cur in enumerate(testcase):
        while stack and cur>testcase[stack[-1]]:
            last = stack.pop()
            answer[last] = i-last
        stack.append(i)
