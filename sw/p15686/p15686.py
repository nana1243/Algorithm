from itertools import combinations
from collections import deque

class chicken:
    def __init__(self):
        self.n,self.m = map(int,input().split(" "))
        self.board = [[] for _ in range(self.n)]
        for i in range(self.n):
            self.board[i] = list(map(int,input().split(" ")))

    def distance(self,house_x,house_y,chicken_x,chicken_y):

        x = abs(house_x - chicken_x)
        y = abs(house_y - chicken_y)
        return x+y



    def chicken_house(self):
        house = []
        chickenhouse = []
        for y in range(self.n):
            for x in range(self.n):
                if self.board[y][x] ==2:
                    res = (x,y)
                    chickenhouse.append(res)
                if self.board[y][x] ==1:
                    res = (x,y)
                    house.append(res)


        return chickenhouse,house


    def solution(self):

        chickenhouse,house = self.chicken_house()
        chickenhouse = deque(list(combinations(chickenhouse,self.m)))

        # 집중에서 최소인 것들이 저장된다

        ans = 100000


        while chickenhouse:
            distance_list = [0 for _ in range(len(house))]
            candidate = chickenhouse.popleft()

            for i in range(len(house)):
                house_x, house_y = house[i][0], house[i][1]
                d = 1000
                for j in range(self.m):
                    chicken_x, chicken_y = candidate[j][0],candidate[j][1]
                    d = min(d,self.distance(house_x,house_y,chicken_x,chicken_y))
                distance_list[i]= d
            ans  = min(ans, sum(distance_list))

        return ans




chicken = chicken()
ans = chicken.solution()
print(ans)


