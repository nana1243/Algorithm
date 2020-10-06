from collections import deque


def solution(bridge_length, weight, truck_weights):
    cross = deque()
    crossing = deque()
    waiting = deque(truck_weights)
    time = 1
    crossing.append([waiting.popleft(), time])

    while crossing:
        if (time - crossing[0][1]) == bridge_length - 1:
            cross.append(crossing.popleft())
        time += 1
        sumlist = 0
        for i in range(len(crossing)):
            sumlist += crossing[i][0]

        if len(waiting) != 0:
            if sumlist + waiting[0] <= weight:
                crossing.append([waiting.popleft(), time])
        else:
            pass

    return time