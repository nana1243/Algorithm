def solution(n, times):
    left = 0
    right = min(times) * n
    ans = 1000000001
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        for i in range(len(times)):
            cnt += mid // times[i]
        if cnt > n:
            right = mid - 1
        elif cnt < n:
            left = mid + 1
        else:
            right = mid - 1

    return left