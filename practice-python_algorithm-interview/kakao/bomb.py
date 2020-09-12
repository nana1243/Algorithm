from collections import deque
import pprint


def countTrue(board, visit, m, n):
    cnt = 0
    for i in range(n): #x
        for j in range(m): #y
            if visit[j][i] == True:
                board[j][i]= 0
                cnt += 1
    return cnt


def makeboard(visit, board, m, n):
    new_board=[]
    for x in range(n):
        stack = []
        for y in range(m):
            stack.append(board[y][x])
        stack = list(filter(lambda x: x != 0, stack))
        while len(stack) != m:
            stack.append(0)
        stack = list(reversed(stack))
        for y in range(m):
            board[y][x] =stack[y]
    return board


def bomb(x, y, visit, board, m, n):
    compare = board[y][x]
    if x - 1 >= 0 and x < n and y >= 0 and y + 1 < m :
        if board[y][x - 1] == compare and board[y + 1][x - 1] == compare and board[y + 1][x] == compare:
            visit[y][x] = True
            visit[y][x - 1] = True
            visit[y + 1][x] = True
            visit[y + 1][x - 1] = True
    return visit


def solution(m, n, board):
    m, n = m, n
    board = deque(board)
    for i in range(m):
        board[i] = deque(list(board[i]))
    visit = [[False for _ in range(n)] for _ in range(m)]
    ans = 0
    cnt = ""

    while cnt != 0:
        for x in range(n):
            for y in range(m):
                if board[y][x]!=0:
                    visit = bomb(x, y, visit, board, m, n)

        cnt = countTrue(board, visit, m, n)
        ans += cnt
        board = makeboard(visit, board, m, n)
        visit = [[False for _ in range(n)] for _ in range(m)]

    return ans


ans=solution(4,5,board=["CCBDE", "AAADE", "AAABF", "CCBBF"])
print(ans)