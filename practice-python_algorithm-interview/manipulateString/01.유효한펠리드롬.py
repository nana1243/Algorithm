# 주어진 문자가 펠리드롬인지 파악해라
# 대소문자 구분이 없음

test = "a man, a plan, a canal: Panama"

def parsing(word):
    result=""
    for elm in word:
        if elm.isalnum():
            result+=elm.lower()
    return list(result)

def isPalidrome(word:list)->bool:

    while len(word)>1:
        if word.pop(0) !=word.pop():
            return False
    return True

def isPalidrome2(word:list):
    return word == word[::-1]


word =parsing(test)
print(isPalidrome2(word))

