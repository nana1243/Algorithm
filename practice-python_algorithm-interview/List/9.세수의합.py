# 배열의 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라


testcase = [-1,0,1,2,-1,-4]

#  부루트포스 => time out
testcase.sort()

def sol1(testcase:list,target):
    ans=[]

    for i in range(len(testcase)-2):
        # 중복된 케이스를 빼기 위해서(중심점이 같으면 같은 결과가 나온다)
        if i>0 and (testcase[i] == testcase[i-1]):
            continue
        for j in range(i+1, len(testcase)-1):
            if j >i+1 and testcase[j]==testcase[j-1]:
                continue
            for k in range(j+1, len(testcase)):
                if k>j+1 and testcase[k] == testcase[k-1]:
                    continue
                if  testcase[i] + testcase[j] + testcase[k] == target:
                    ans.append([testcase[i] ,testcase[j] ,testcase[k]])

    return ans


# 포인터로 계산


def sol2(testcase:list,target):
    ans = []
    for i in range(len(testcase) - 2):
        # 중복된 케이스를 빼기 위해서(중심점이 같으면 같은 결과가 나온다)
        if i > 0 and (testcase[i] == testcase[i - 1]):
            continue

        check = target - testcase[i]
        left ,right = i+1, len(testcase)-1

        while left<right:
            if testcase[left] + testcase[right] > check:
                right-=1

            elif testcase[left] + testcase[right]<check:
                left +=1

            else:
                ans.append([testcase[i],testcase[left],testcase[right]])

                while left< right and testcase[left] == testcase[left+1]:
                    left+=1
                while left< right and testcase[right] == testcase[right-1]:
                    right-=1

                left+=1
                right-=1

    return ans


print(sol2(testcase,0))














