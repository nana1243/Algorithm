from collections import deque
from pprint import pprint
n = int(input())

board =[[0 for i in range(n)] for _ in range(n)]

k = int(input())
for i in range(k):
    y,x = map(int,input().split(" "))
    board[y-1][x-1] = 1

pprint(board)

command = deque([])
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
    if (cur_x == next_x) and (cur_y== next_y):
        return True
    return False

# changedirection을
def move(direction,time):
    cnt=0

    for i in range(1,time+1):
        cur_x, cur_y = curr.pop()
        cnt+=1
        next_x = cur_x+direction[0]
        next_y = cur_y+direction[1]
        if finish(cur_x,cur_y,next_x,next_y) == False:
            if board[next_y][next_x]==1:
                board[next_y][next_x]=0
                curr.append([cur_x,cur_y])
                curr.append([next_x,next_y])
            else:
                curr.clear()
                curr.append([next_x,next_y])
        else:
            return True,cnt



    return False,cnt

def changedirection(direction,command_direction):
    d  =[(1,0),(0,1),(-1,0),(0,-1)]
    idx = d.index(direction)
    if command_direction=="D":
        result = d[idx+1]
    else:
        result = d[idx-1]
    return result


def solution():
    direction=(1,0)
    ans=0

    while command:
        print(curr)
        time, command_direction = command.popleft()
        finish,cnt = move(direction,time)
        print(finish,cnt)
        if finish==True:
            ans+=cnt
            break
        else:
            ans+=cnt
            direction = changedirection(direction,command_direction)


    return ans


print(solution())




