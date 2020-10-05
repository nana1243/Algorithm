from collections import deque
from pprint import pprint
n = int(input())

board =[[0 for i in range(n)] for _ in range(n)]

k = int(input())
for i in range(k):
    y,x = map(int,input().split(" "))
    board[y-1][x-1] = 1


start = [0,"D"]
command = deque([start])
for i in range(int(input())):
    time,direction = input().split(" ")
    command.append([int(time), direction])

curr=deque([[0,0]])

# 1. finish조건이 끝날때까지 이 일을 반복한다
# 2. curr에 현재위치를 뽑는다 , prev 위치도 뽑는다 만약 board==1: curr먼저 넣고 next를 넣는다
# 3. board 가 ==0이라면 next위치만 ㅃ뽀늗


def finish(cur_x, cur_y,next_x,next_y):
    if next_x<0 or next_x>n-1 or next_y<0 or next_y>n-1:
        return True
    if (cur_x == next_x) and (cur_y == next_y):
        return True
    return False

# changedirection을

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

def move(direction:tuple,prev_time,time):
    cnt=0
    for i in range(prev_time,time):
        cnt+=1
        next_x = curr[-1][0] + direction[0]
        next_y = curr[-1][1] + direction[1]

        if finish(curr[-1][0], curr[-1][1], next_x, next_y) == True:
            return True,cnt
        if board[next_y][next_x] == 1:
            board[next_y][next_x]=0
            curr.append([next_x,next_y])
            if len(curr) > 2:
                curr.popleft()

        else:
            curr.clear()
            curr.append([next_x,next_y])

    return False,cnt

def changedirection(direction,command_direction):
    d  =[(1,0),(0,1),(-1,0),(0,-1)]
    idx = d.index(direction)
    if command_direction == "D":
        result = d[idx+1]
    else:
        result = d[idx-1]
    return result


def solution():
    direction=(1,0)
    ans=0

    while command:
        time,command_direction = command.popleft()
        direction = changedirection(direction, command_direction)
        try:
            finish,cnt = move(direction, time ,command[0][0])
        except IndexError:
            finish,cnt = move(direction,time,100)
        if finish == True:
            ans+=cnt
            break
        else:
            ans+=cnt

    return ans


print(solution())




