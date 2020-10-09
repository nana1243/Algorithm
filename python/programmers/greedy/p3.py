# 정방향으로 joistic을 움직인 경우
# testcase -1

def move(target):
    if target == "A":
        return 0
    rmove = ord(target) - ord("A")
    lmove = ord("Z") - ord(target) + 1
    ans = min(rmove, lmove)
    return ans


def joistic(name):
    n = len(name)
    start = "A" * n
    ans = 0
    for i in range(n):
        if name[i:] == "A" * len(name[i:]):
            return ans - 1
        ans += 1
        result = move(name[i])
        ans += result
    return ans - 1


def solution(name):
    n = len(name)
    if name == "A" * n:
        return 0
    leftname = name[0] + ''.join(elm for elm in reversed(name[1:]))
    rightscore = joistic(name)
    leftscore = joistic(leftname)
    ans = min(rightscore, leftscore)

    return ans