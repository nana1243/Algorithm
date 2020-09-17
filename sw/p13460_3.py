
# 1. 이론적으로 정리해야할 것 ->  bfs가 왜 que를 썼었는지 check
# 2. 못품


##########################################################################################
# 3. 왜 못풀겠는지 적어보자
#1. 빨간색공과 파란색공이 겹치는 그 로직을 어떻게 풀어야 할지 정확하게 모르겟음
#2. 그렇다면 => 일단 그 경우를 제외하고 풀어보고 => 그다음 추가해보자 => 사람들 푼거 보고 해결

#3. 그리고 for문돌리는 것까진 괜찮은데 1번 testcase처럼 옆에 o가 있고 위로 .이 존재할땐
#4. 그때를 제지하는 로직은?
#5. 진짜 짜증나!!!!!!왜안풀리고난리야 진짜레알짜증나

##########################################################################################
##########################################################################################
# 1. q에 원소를 뺀다
# 2. 방향을 정해서 갈수 있는데 까지 간다
# 3. 그리고 파란색과 빨간색의 거리를 비교한다(why? 동시에 같은 공이 있을 수 없으니깐)
# 3-1. 만약 파랑색의 공의 길이가 더 길다면 빨간색은 rollback 시킨다
# 4. ans+=1시킨다
# 5. target을 만나면그자리에서 끝낸다 (빨간색일경우)
# 6. 파란색이 target이 될경우 => -1이된다
# 7. 큐에 마지막 지점을 넣는다
############################################################################################

from collections import deque
class Escape:

    def __init__(self):
        self.n, self.m = map(int,input().split(" "))
        self.board = [[] for _ in range(self.n)]
        self.red = None
        self.blue = None
        self.target = None
        self.visit=[[False for _ in range(self.m)] for _ in range(self.n)]


    def rule(self, x , y):
        if  y >= 0 and y < self.n and x>=0 and x<self.m :
           return True
        return False


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


    def bfs(self):

        self.makeboard()

        red_x,red_y ,blue_x, blue_y = self.red[0],self.red[1],self.blue[0],self.blue[1]
        start = [red_x,red_y,blue_x,blue_y]
        q=deque([start])

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        ans=0


        while ans<10 and q :
            red_x,red_y,blue_x,blue_y = q.popleft()

            if ans>10:
                break

            for i in range(4):
                new_red_x = red_x + dx[i]
                new_red_y = red_y  + dy[i]
                new_blue_x = blue_x  + dx[i]
                new_blue_y = blue_y  + dy[i]

                rcnt,bcnt=0,0



                while  self.rule( new_red_x,new_red_y) ==True and\
                    self.board[new_red_y][new_red_x]!="#" and \
                    self.board[new_red_y][new_red_x] != "O":

                    new_red_x+=dx[i]
                    new_red_y+=dy[i]
                    rcnt+=1

                while self.rule(new_blue_x,new_blue_y)==True and self.board[new_blue_y][new_blue_x] != "#" and \
                        self.board[new_blue_y][new_blue_x] != "O":
                    new_blue_x += dx[i]
                    new_blue_y += dy[i]
                    bcnt += 1

                if new_red_x == self.target[0] and new_red_y == self.target[1]:
                    ans+=1
                    return ans

                if new_red_y == new_blue_y and new_red_x == new_red_y:
                    if bcnt>rcnt:
                        new_blue_x -=dx[i]
                        new_blue_y -= dy[i]
                    else:
                        new_red_y -= dy[i]
                        new_red_x -= dx[i]


                if self.visit[new_red_y][new_red_x]==False:
                    self.visit[new_red_y][new_red_x] =True
                    ans+=1
                    q.append([new_red_x,new_red_y,new_blue_x,new_blue_y])

        return ans





e = Escape()
ans=e.bfs()
print(ans)




