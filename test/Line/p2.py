from collections import deque


# 1. order을 뺀다
# 2-1. order의 번호가 공의 양끝에 존재하면 ans.append()
# 2-1-1 빼고난 공에 waiting이 존재하면 없어질때까지 반복
# 2-2. 그렇지 안흐면 waiting에 넣는다
# 공이 없어질때까지 이 과정을 반복한다

def solution(ball, order):
    order.reverse()
    ball = deque(ball)
    waiting =deque([])
    ans=[]

    while ball:
        out = order.pop()
        if ball[0] == out:
            ans.append(ball.popleft())
            while len(ball)!=0  and ball[0] in waiting:
                ans.append(ball.popleft())
        elif ball[-1]  == out:
            ans.append(ball.pop())
            while len(ball)!=0 and ball[-1] in waiting:
                ans.append(ball.pop())
        else:
            waiting.append(out)


    return ans


print(solution([1, 2, 3, 4, 5, 6],order=[6, 2, 5, 1, 4, 3]))

print(solution(ball=[11, 2, 9, 13, 24], order=[9, 2, 13, 24, 11]))