

# 2-9까지 숫자가 주어졌을때 전화번호로 조합 가능한 모든 문자를 출력하라
test="23"
hashmap={
    '2':"ABC",
    '3':"DEF",
    '4':"GHI",
    '5':"JKL",
    '6':"MNO",
    '7':"PQRS",
    '8':"TUV",
    '9':"WXYZ"
}
# 모든 숫자의 조합
result=[]
def dfs(index,path):
    if len(path)==len(test):
        result.append(path)
    for i in range(index,len(test)):
        for elm in hashmap[test[i]]:
            dfs(i+1,path+elm)


    return result

print(dfs(0,""))


