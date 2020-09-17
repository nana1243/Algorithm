# 각각의 동작에서 공은 동시에 움직인다.
# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
# 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.



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


    def move(self,new_x,new_y):
        pass



    def bfs(self):
        red_x,red_y ,blue_x, blue_y = self.red[0],self.red[1],self.blue[0],self.blue[1]
        q=deque([red_x,red_y,blue_x,blue_y])
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        ans=0

        while q and ans<10:
            red_x,red_y,blue_x,blue_y=q.popleft()

            for i in range(4):
                new_red_x = red_x + dx[i]
                new_red_y = red_y + dy[i]

                new_blue_x = blue_x + dx[i]
                new_blue_y = blue_y + dy[i]

                if self.board[new_red_y][new_red_x]=="O":
                    return

                elif self.board[new_red_y][new_red_x]==".":

                    pass
                else:
                    # stop
                    pass






    def solution(self):
        pass