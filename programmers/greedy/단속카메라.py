def solution(routes):
    routes = sorted(routes)
    answer = 0
    last_camera = 30000
    print(routes)

    for route in reversed(routes):
        if last_camera > route[1]:
            answer += 1
            last_camera = route[0]
    return answer