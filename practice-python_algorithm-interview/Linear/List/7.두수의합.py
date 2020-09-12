
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴해라

testcase=[2,7,11,15]
target = 9



def sol1(testcase:list,target:int) :
    for i,elm in enumerate(testcase):
        lookfor = target - elm

        if lookfor in testcase[i+1:]:
            return [i, testcase.index(lookfor)]

print(sol1(testcase,target))


# hashmap사용(return에 대한 최적화)

def sol2(testcase:list,target:int):
    hashmap ={elm:i for i,elm in enumerate(testcase) }

    for idx,elm in enumerate(testcase):
        lookfor = target-elm
        if lookfor in hashmap and idx!=hashmap[lookfor]:
            return idx, hashmap[lookfor]


print(sol2(testcase,target))

# 인덱스를 묻는 문제에서는 포인터를 사용하는 경우가 힘들다



