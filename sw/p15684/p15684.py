from itertools import combinations
from collections import deque
from copy import deepcopy
from pprint import pprint
from collections import defaultdict
import sys

class ladder:
    def __init__(self):
        self.n,self.m, self.h = map(int,sys.stdin.readline().split(" "))
        self.board = [[0 for _ in range(self.n)] for _ in range(self.h)]
        self.graph = {}
        for _ in range(self.m):
            y, x= map(int,sys.stdin.readline().split(" "))
            self.board[y-1][x-1] = 1
            self.board[y-1][x] = 1
            key = (x-1) + (y-1)*self.n
            values = key+1
            self.graph[key] = values


    def move(self,x,board,v):
        new_visited = [[False for _ in range(self.n)] for _ in range(self.h)]
        start =0

        while start<self.h:
            for y in range(start,self.h):
                key = x+ y*self.n
                if key-1 in v and x>0 and board[y][x]==1 and board[y][x-1]==1 and new_visited[y][x]==False :
                    new_visited[y][x] = True
                    new_visited[y][x - 1] = True
                    start = y
                    x = x - 1
                    break

                elif key in v and x < self.n-1 and board[y][x]==1 and board[y][x+1]==1 and new_visited[y][x]==False:
                    new_visited[y][x] = True
                    new_visited[y][x + 1] = True
                    start = y
                    x = x + 1
                    break
                else:
                    start+=1
            if start >= self.h-1:
                break
        return x

    def choose(self):
        candidate= set()
        for y in range(self.h):
            for x in range(self.n-1):
                if self.board[y][x]==0 and self.board[y][x+1]==0 :
                    res = (x,y)
                    candidate.add(res)
        return candidate

    def check(self,checklist):
        for elm,idx in enumerate(checklist):
            if idx!=elm:
                return False
        return True

    def solution(self):
        candidate = self.choose()

        checklist =[]
        for i in range(self.n):
            res = self.move(i,self.board,self.graph)
            checklist.append(res)

        if self.check(checklist)==True:
            return 0

        ans =-1
        cnt=1

        while cnt<4:
            c = deque(combinations(candidate,cnt))
            while c:
                checklist = []
                tmp = deepcopy(self.board)
                v = deepcopy(self.graph)
                out =c.popleft()

                for elm in out:
                    x,y = elm[0],elm[1]
                    key = x +(y*self.n)
                    if key-1 not in v  and x<self.n-1:
                        v[key] = key+1
                        tmp[y][x] = 1
                        tmp[y][x + 1] = 1

                for i in range(self.n):
                    res = self.move(i, tmp,v)
                    checklist.append(res)


                if self.check(checklist)==True:
                    return cnt

            cnt+=1

        return ans





test = ladder()
ans = test.solution()
print(ans)

