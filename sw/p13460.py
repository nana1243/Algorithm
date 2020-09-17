
# 못풀겟다
from collections import deque
class Escape:

    def __init__(self):
        self.n, self.m = map(int,input().split(" "))
        self.board = [[] for _ in range(self.n)]
        self.red = None
        self.blue = None
        self.target = None
        self.visit=[[False for _ in range(self.m)] for _ in range(self.n)]


    def makeboard(self):
        for i in range(self.n):
            readline = list(input())
            self.board[i] = readline
            if "R" in readline:
                self.red = [readline.index("R"),i]
            if "B" in readline:
                self.blue = [readline.index("B"),i]
            if "O" in readline:
                self.target = [readline.index("O"),i]

        self.visit[self.red[1]][self.red[0]] = True
        self.visit[self.blue[1]][self.blue[0]] = True

    def move(self,cur_x,cur_y,dx,dy,long):

        while self.board[cur_y+dy][cur_x+dx]!="#" and self.board[cur_y+dy][cur_x+dx]!="O":
            cur_x+=dx
            cur_y+=dy
            long+=1

        return  cur_x,cur_y,long

    def bfs(self):
        red_x,red_y,blue_x,blue_y = self.red[0],self.red[1],self.blue[0],self.blue[1]
        q=deque([red_x,red_y,blue_x,blue_y])

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        self.visit[blue_y][blue_x] = True
        self.visit[red_y][red_x] = True

        while q :
            if ans>10:
                return -1

            red_x,red_y,blue_x,blue_y,ans = q.popleft()
            for i in range(4):
                red_x,red_y,rcnt = self.move(red_x,red_y,dx[i],dy[i],0)
                blue_x,blue_x,bcnt=self.move(blue_x,blue_y,dx[i],dy[i],0)


            if self.board[blue_y][blue_x]=="O":
                continue

            if self.board[red_y][red_x] =="O":
                return ans







