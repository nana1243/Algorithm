
# 답지를 봐도 왜 이문제를 bfs로 푸는지 잘 모르겠다..ㅜㅜㅜㅜ


import sys
from collections import deque

class Escape:
    def __init__(self,n,m):
        self.n = n  #세로
        self.m = m  # 가로
        self.board = [[] for _ in range(n)]
        self.red = [0,0]
        self.blue = [0,0]
        self.target= [0,0]
        self.visit = [[False for _ in range(self.m)] for _ in range(self.n)]

    def makeboard(self):
        for i in range(self.n):
            readline = list(map(int,sys.stdin.readline()))
            self.board[i] = readline
            if "R" in readline:
                self.red = [readline.index("R"),i]
            if "B" in readline:
                self.blue = [readline.index("B"),i]
            if "O" in readline:
                self.target = [readline.index("O"),i]


    def rule(self,x,y):
        if x<0 or x>self.m-1 or y<0 or y>self.n-1:
            return False
        return True



    def move(self,cur_x,cur_y,dx,dy):

        while self.rule(cur_x,cur_y)==True:
            self.visit[cur_y][cur_x] = True
            if self.board[cur_y][cur_x] == "#" or self.board[cur_y][cur_x] == "O":
                break
            cur_x = cur_x + dx
            cur_y = cur_y + dy

        return cur_x,cur_y

    def bfs(self,cur_x,cur_y):
        start = [cur_x,cur_y]
        que =deque([start])

        dx =[1,-1,0,0]
        dy = [0,0,1,-1]

        while que:
            out = que.popleft()
            self.visit[cur_y][cur_x] = True

            for i in range(4):
                new_x = cur_x + dx[i]
                new_y = cur_y + dy[i]

                if self.rule(new_x,new_y) ==True and self.visit[new_y][new_x]==False:
                    self.move(new_x,new_y,dx[i],dy[i])


    def solution(self):

        self.makeboard()
        red_x, red_y = self.red[0],self.red[1]
        blue_x, blue_y = self.blue[0],self.blue[1]

