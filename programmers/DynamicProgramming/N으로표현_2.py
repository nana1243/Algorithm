def operator(m, n):  # m이 이전수
    plus = m + n
    minus = m - n
    multi = m * n
    if n != 0 and m % n == 0:
        div = m // n
        return [plus, minus, multi, div]
    else:
        return [plus, minus, multi]

def solution(N, number):
    ans = [[] for _ in range(N+1)]
    ans[0].append(N)
    if ans[0] == number:
        return 1
    for i in range(1, N + 1):
        for j in range(len(ans[i - 1])):
            input=operator(ans[i - 1][j],N)
            ans[i]+=input
            ans[i].append(int(str(N)*(i+1)))
        if number in ans[i]:
            return i+1

print(solution(2,11))

