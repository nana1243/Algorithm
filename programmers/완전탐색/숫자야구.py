baseball=[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

baseball.sort(key=lambda x:x[1], reverse=True)
print(baseball)
### 두가지 요소 고려하는 숫자 sort 하는 법 체크하기
### 327 중 두가지 숫자만 맞다 -> 32x,x27,3x7
### 123 중 한가지 숫자는 자릿수까지 같고 나머지 한개는 숫자만 같고 나머지는 다다르다
###### 32x  임을 알 수 있다
### 356에서  한자리는 동일하다 32x
#### 숫자만 동일하고 자리는 다르다 324, 328 ->2가지가 된다

# from itertools import permutations
# cases=[]
#
# def rule(number:list):
#     n=number[0]
#     strike=number[1]
#     ball=number[2]
#     if strike !=0:
#         cases = list(("".join(item)) for item in set(permutations(str(n), strike)))
#         return cases
#     if ball !=0:



print(rule([327,2,0]))
