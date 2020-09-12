# 로그를 재정렬하라

#1.로그의 가장 앞부분은 식별자이다
#2. 문자로 구성된 로그가 숫자로그보다 앞선다
#3. 식별자는 순서에 상관없지만, 문자가 동일한경우 식별자 순으로 한다
#4. 숫자로그는 입력순서대로 한다

def reorderLogFiles(logs:list):
    letters,digits=[],[]

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key= lambda x: (x.split()[1:],x.split()[0]))

    return letters + digits

logs =["dig1 8 1 5 1","let1 art can"]

print(reorderLogFiles(logs))
