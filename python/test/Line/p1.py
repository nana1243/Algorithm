

from collections import Counter
import math


def counter(boxes):
    total_element = []
    for box in boxes:
        total_element += box[0], box[1]
    counter = Counter(total_element)
    counter = dict(filter(lambda x: x[1] != 2, counter.items()))
    return counter



def solution(boxes):
    c_box = counter(boxes)
    print(c_box)
    answer = math.ceil(len(c_box) / 2)

    return answer

boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
print(solution(boxes))