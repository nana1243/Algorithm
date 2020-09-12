"""
a-z로 표현된 테스크가 있다. cpu는 한번의 테스크만 실행할 수 있고,
n번의 간격 내에는 동일한 테스크를 실행시킬 수 없다
"""

tasks1=["A","A","A","B","B","B"]
tasks2=["A","A","A","B","C","D"]
n=2
from collections import Counter

# 우선순위 큐 사용
def leastInterval(tasks:list):
    counter = Counter(tasks)
    result=[]
    cnt=0

    while counter:

        for elm,_ in counter.most_common(n+1):

            result.append(elm)
            counter.subtract(elm)
            counter +=Counter()
        if not counter:
            break

        result.append("idle->")
    return result


print(leastInterval(tasks2))