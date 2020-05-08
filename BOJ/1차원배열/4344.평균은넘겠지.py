n=int(input())

for i in range(n):
    testcase=list(map(int,input().split(" ")))
    num=testcase[0]
    testcase=testcase[1:]
    avg = sum(testcase) / num
    cnt = 0
    for i in range(len(testcase)):
        if testcase[i] > avg:
            cnt += 1
    print("%.3f" %((cnt / num) * 100)+"%")


