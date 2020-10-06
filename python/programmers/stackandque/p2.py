from math import ceil
from collections import deque


def complete(progress, speed):
    remainder = ceil((100 - progress) / speed)
    return remainder


def solution(progresses, speeds):
    complete_day = deque([])
    ans = []

    for i in range(len(progresses)):
        res = complete(progresses[i], speeds[i])
        complete_day.append(res)

    while complete_day:
        cnt = 1
        compare = complete_day.popleft()
        for i in range(len(complete_day)):
            if compare >= complete_day[0]:
                cnt += 1
                complete_day.popleft()
            else:
                break
        ans.append(cnt)

    return ans