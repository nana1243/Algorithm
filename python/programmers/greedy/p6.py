# 모든 차량이 한번은 단속용 카메라를 만나도록 하려면 최소 몇대의 카메라를 설치해야 하는가


def solution(routes):
    routes.sort(key=lambda x: x[0])
    routes = routes
    cnt = 1

    left = routes[0][0]
    right = routes[0][1]
    for i in range(1, len(routes)):
        newleft = routes[i][0]
        newright = routes[i][1]
        if right < newleft:
            right = newright
            cnt += 1
        if right > newright:
            right = newright
        left = newleft

    return cnt