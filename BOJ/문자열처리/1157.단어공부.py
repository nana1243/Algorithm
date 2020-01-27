# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# word="Mississipi"
# word="zZa"


# 가장 많은 빈도수

word=input()
from collections import Counter
result=Counter(word.upper())
if len(result)>1:
    if result.most_common(2)[0][1]==result.most_common(2)[1][1]:
        print("?")
    else:
        print(result.most_common(1)[0][0])
else:
    print(result.most_common(1)[0][0])



