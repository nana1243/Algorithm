def solution(words):
    myDic = {}
    words.sort() # 길이에 따른 sort
    i = 0
    while i < len(words):
        if i==0:
            myDic[words[i]] = words[i][0]
        else :
            insec = compareString(words[i-1], words[i])
            if len(insec) == 0:
                myDic[words[i]] = words[i][0]
            elif insec == words[i-1]:
                myDic[insec] = insec
                myDic[words[i]] = words[i][:len(insec)+1]
            elif len(insec) >= len(myDic[words[i-1]]):
                myDic[words[i-1]] = words[i-1][:len(insec)+1]
                myDic[words[i]] = words[i][:len(insec)+1]
            else :
                myDic[words[i]] = words[i][:len(insec)+1]
        i += 1
    return sum([len(myDic.get(word)) for word in words])

def compareString(prev, curr):
    i  = 0
    while i < len(prev): # 이전의 글자의 길이가 길때까지 이과정을 반복하여러
        if prev[i] != curr[i]:
            break
        i += 1
    return prev[:i]