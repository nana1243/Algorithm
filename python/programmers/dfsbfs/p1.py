class Number:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.n = len(numbers)
        self.answer = 0

    def dfs(self, idx, value):
        if (idx == self.n - 1):
            if value == self.target:
                self.answer += 1
            return
        self.dfs(idx + 1, value + self.numbers[idx + 1])
        self.dfs(idx + 1, value - self.numbers[idx + 1])


def solution(numbers, value):
    n = Number(numbers, value)
    n.dfs(0, numbers[0])
    n.dfs(0, -numbers[0])
    return n.answer