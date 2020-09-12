# n개의 페어(pair)를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수

# min의 합이 가장 크기 위해서는 작은 것들끼리 묶어놔야 한다
testcase= [1,4,3,2,5,6,7,8,9,10]

def sol1(testcase:list):
    testcase.sort()
    result=0
    pair=[]
    for elm in testcase:
        pair.append(elm)
        if len(pair)==2:
            result+=min(pair)
            pair=[]
    return result

print(sol1(testcase))

def sol2(testcase:list):
    testcase.sort()
    result=0
    for idx, elm in enumerate(testcase):
        if idx %2 ==0:
            result+=elm
    return result

print(sol2(testcase))

def sol3(testcase:list):
    testcase.sort()
    return sum(testcase[::2])

print(sol3(testcase))