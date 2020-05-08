from collections import deque

priorities=[9,1, 1, 9, 1, 1, 1]

result=deque()

for element in enumerate(priorities):
    result.append(element)

cnt=1
idx=1
print(result)


