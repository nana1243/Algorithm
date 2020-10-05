# dictionary sort
## 1. 둘다 values값에 따른 key sort

genres_score=sorted(genres_score.items(),reverse=True,key=lambda item: item[1])
g = sorted(g.keys(), key=lambda x: g[x], reverse=True)


from functools import reduce
## 2. reduce 함수 : reduce( function ,list, 가장 초기값)
## 언제쓰이냐?-> 누적일때

answer=reduce(lambda x,y: x*(y+1), clothes_number.values(),1)-1
##ex2>
a=[5,4,3,2,1]
answer = reduce(lambda x,y : x*y , a,1 )



### 접두사(?)가 같은 문제
### 1. string.startswith(기준이되는 string)
### 2. sort()를 통해 가장 짧은것부터 비교해야한다


### counter함수
## n차원list의 원소를 counter쓰고 싶을때
from collections import Counter

clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes_number=Counter(element[1] for element in clothes)
