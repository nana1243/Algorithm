from collections import deque


def solution(p, l):
    p = deque([(idx, elm) for idx, elm in enumerate(p)])
    ans = []

    while p:

        out = p.popleft()
        if any(out[1]<elm[1] for elm in p ):
            p.append(out)
        else:
            ans.append(out)
            if out[0]==l:
                return len(ans)




p=[1, 1, 9, 1, 1, 1]
l=0

ans = solution(p,l)
print(ans)