import sys

from pprint import pprint

class dust:
    def __init__(self):
        self.R,self.C,self.T = map(int,sys.stdin.readline().split(" "))
        self.board = [ [] for _ in range(self.R)]
        for i in range(self.R):
            self.board[i] = list(map(int,sys.stdin.readline().split(" ")))

    def diffusion(self,cur_x,cur_y):
        t= [[1,0],[-1,0],[0,1],[0,-1]]

        total = self.board[cur_y][cur_x]
        out = total//5

        for i in range(4):
            new_x = cur_x + t[i][0]
            new_y = cur_y + t[i][1]

            if 0<=new_x<self.C and 0<=new_y<self.R:
                if self.board[new_y][new_x]!=-1:
                    self.board[new_y][new_x] = out
                    self.board[cur_y][cur_x] -= out


    def clean(self,cur_x,cur_y,time):
        t =[[1,0],[0,1],[-1,0],[0,-1]]


        while time<self.T:
            self.board[cur_y][cur_x] = self.board[cur_y][cur_x-1]













    def solution(self):
        pprint(self.board)


d =dust()
d.solution()