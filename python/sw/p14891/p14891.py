import sys

# 이문제는 try except 를 통해 rotate함수를 하나로 쓸수 도 있을 것 같은데

class Wheel:
    def __init__(self):
        self.first = list(sys.stdin.readline().strip())
        self.second = list(sys.stdin.readline().strip())
        self.third = list(sys.stdin.readline().strip())
        self.fourth = list(sys.stdin.readline().strip())
        self.n = int(input())
        self.cmd = []

    def rotate(self, direction, l):
        new_l = []

        if direction == 1:
            new_l += list(l[-1]) + l[:-1]
        else:
            new_l += l[1:] + list(l[0])
        return new_l

    def inputcmd(self):
        for i in range(self.n):
            number, direction = map(int, sys.stdin.readline().split(" "))
            self.cmd.append([number, direction])

    def score(self):
        ans = 0
        if self.first[0] == '1':
            ans += 1
        if self.second[0] == '1':
            ans += 2
        if self.third[0] == '1':
            ans += 4
        if self.fourth[0] == '1':
            ans += 8
        return ans

    def rotate_first(self, direction):
        first = self.first[::]
        second = self.second[::]
        third = self.third[::]
        fourth = self.fourth[::]

        self.first = self.rotate(direction, self.first)
        if first[2] != second[6]:
            self.second = self.rotate(-direction, self.second)
            if second[2] != third[6]:
                self.third = self.rotate(direction, self.third)
                if third[2] != fourth[6]:
                    self.fourth = self.rotate(-direction, self.fourth)
            else:
                return
        else:
            return
        return

    def rotate_second(self, direction):
        first = self.first[::]
        second = self.second[::]
        third = self.third[::]
        fourth = self.fourth[::]

        self.second = self.rotate(direction, self.second)
        if first[2] != second[6]:
            self.first = self.rotate(-direction, self.first)
        if second[2] != third[6]:
            self.third = self.rotate(-direction, self.third)
            if third[2] != fourth[6]:
                self.fourth = self.rotate(direction, self.fourth)
        else:
            return
        return

    def rotate_third(self, direction):
        first = self.first[::]
        second = self.second[::]
        third = self.third[::]
        fourth = self.fourth[::]

        self.third = self.rotate(direction, self.third)

        if third[2] != fourth[6]:
            self.fourth = self.rotate(-direction, self.fourth)

        if third[6] != second[2]:
            self.second = self.rotate(-direction, self.second)
            if second[6] != first[2]:
                self.first = self.rotate(direction, self.first)
            else:
                return
        else:
            return

    def rotate_fourth(self, direction):
        first = self.first[::]
        second = self.second[::]
        third = self.third[::]
        fourth = self.fourth[::]

        self.fourth = self.rotate(direction, self.fourth)

        if fourth[6] != third[2]:
            self.third = self.rotate(-direction, self.third)
            if second[2] != third[6]:
                self.second = self.rotate(direction, self.second)
                if first[2] != second[6]:
                    self.first = self.rotate(-direction, self.first)
            else:
                return
        else:
            return
        return

    def solution(self):
        self.inputcmd()
        for elm in self.cmd:
            wheel_number, direction = elm[0], elm[1]
            if wheel_number == 1:
                self.rotate_first(direction)
            elif wheel_number == 2:
                self.rotate_second(direction)
            elif wheel_number == 3:

                self.rotate_third(direction)
            else:
                self.rotate_fourth(direction)

        ans = self.score()

        return ans


w = Wheel()
print(w.solution())

