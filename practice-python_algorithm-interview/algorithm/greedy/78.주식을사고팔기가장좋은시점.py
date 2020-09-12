
"""
여러번의 거래로 낼 수 있는 최대의 이익을 구하여라

이전보다 오르면 판다 그것이 누적되면 마지막 오르는 지점에 사는 것과 동일하게 된다
"""

testcase=[7,1,5,3,6,4]

def makeprofit(cost):
    result=0

    for i in range(len(cost)-1):
        if cost[i+1]>cost[i]:
            result+=cost[i+1] -cost[i]
    return result


# 해당 코드에 대한 최적화를 해보자
# 성능에 차이는 없지만 , 파이썬다운 방식으로 정리할 수 있다
def makeprofit2(cost):

    return sum( max(cost[i+1]-cost[i],0) for i in range(len(cost)-1))