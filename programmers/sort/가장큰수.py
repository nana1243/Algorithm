# 기억해야할 것
## 숫자비교 방법론(앞자리가 큰숫자인것을 우선순위1, 그다음자리 숫자를 우선순위2)

def solution(numbers):
    numbers=sorted(numbers, key=lambda x: -int((str(x)*4)[:4]))
    answer=""
    for element in numbers:
        answer+=str(element)
    if answer[0]=='0':
        return "0"
    else:
        return answer

