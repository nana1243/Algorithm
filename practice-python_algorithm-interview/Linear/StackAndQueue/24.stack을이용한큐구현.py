# 스택을 이용하여 큐를 구현하라

class MyQueue:
    def __init__(self):
        self.input =[]
        self.output=[]

    def push(self,item):
        self.input.append(item)

    def pop(self):
        self.peek()
        return self.output.pop()


    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]

    def empty(self):
        return self.input ==[] and self.output ==[]