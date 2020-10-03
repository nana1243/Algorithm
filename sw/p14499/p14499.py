from collections import deque

n,m,cur_y,cur_x,order = map(int,input().split(" "))
board=[[] for _ in range(n)]
dice =[0 for _ in range(6)]

for i in range(n):
    board[i] = list(map(int,input().split(" ")))

cmd = deque(list(map(int,input().split(" "))))

def move(direction):
    d=[[1,0],[-1,0],[0,-1],[0,1]]
    return d[direction-1]


def makedice(direction,dice):
    if direction ==4:
        tmp=[dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    elif direction ==3: # 북쪽
        tmp = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    elif direction ==1:
        tmp = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    else: #서쪽
        tmp = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    dice = tmp
    return dice

# 1. 명령에 따라 움직인다
# 2-1. 움직인 자리의 숫자가 0이면 , 주사위의 바닥면에 숫자로 칸 복사
# 2-2. 움직인 자리의 숫자가 0이아닌경우, 칸에 쓰여진 숫자가 주사위로 복사가 되고 칸에 쓰여있는 수가 0이된다
# 3. 이때 주사위의 상단 숫자가 출력시킨다


while cmd:
    order = cmd.popleft()
    toward =move(order)
    cur_x += toward[0]
    cur_y += toward[1]

    if cur_x<0 or cur_x >m-1 or cur_y <0 or cur_y>n-1:
        cur_x = cur_x-toward[0]
        cur_y = cur_y-toward[1]
        continue
    else:
        if board[cur_y][cur_x] != 0:
            dice = makedice(order, dice)
            print(dice[0])
            new_number = board[cur_y][cur_x]
            dice[5] = new_number
            board[cur_y][cur_x] = 0
        elif board[cur_y][cur_x]==0:
            dice = makedice(order, dice)
            print(dice[0])
            new_number = dice[5]
            board[cur_y][cur_x] = new_number
