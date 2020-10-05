def solution(money):
    cache0 = [money[0], money[0]] # 0번째 요소를 고르고 시작한 경우
    cache1 = [0, money[1]] # 0번째 요소를 고르지 않고 시작한 경우

    for i in range(2, len(money)-1):
        cache0.append(max(cache0[i-2] + money[i], cache0[i-1]))

    for i in range(2, len(money)):
        cache1.append(max(cache1[i-2] + money[i], cache1[i-1]))

    return max(cache0[-1], cache1[-1])