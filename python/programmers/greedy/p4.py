from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)
    ans = 0

    while people:
        ans += 1
        weight = 0
        cnt = 0
        while cnt < 2 and len(people) != 0:
            if people[0] + weight > limit:
                break
            else:
                weight += people.popleft()
            cnt += 1

    return ans