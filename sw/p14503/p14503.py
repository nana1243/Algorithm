n, m = map(int, input().split(" "))
cur_x, cur_y, direction = map(int, input().split(" "))
board = [[] for _ in range(n)]
for i in range(len(board)):
    board[i] = list(map(int, input().split(" ")))
ans=0
###################################################################################

# 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

# rule 1,2
def clean(cur_x,cur_y,direction):
    global  ans
    toward = move(direction)
    while board[cur_y][cur_x] != 1:
        board[cur_y][cur_x] = 0
        ans+=1
        cur_x += toward[0]
        cur_y += toward[1]

    return  cur_x,cur_y


def solution(cur_x,cur_y):
    toward = move(direction)
    if rule_a(cur_x,cur_y,toward)==True:
        pass



def rule_a(cur_x,cur_y,toward):
    check = False
    while True:
        cur_x += toward[0]
        cur_y += toward[1]
        try:
            if board[cur_y][cur_x] == 1:
                check = True
                break
        except IndexError:
            break

    return check




def move(direction):
    d = [[0,1],[1,0],[0,-1],[-1,0]]
    return d[direction-1]

def changedirction(toward):
    d = [[0,1],[1,0],[0,-1],[-1,0]]
    result =d.index(toward)
    return result+1
