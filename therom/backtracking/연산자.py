##### backtracking#########


n = int(input())
testcase = list(map(int,input().split(" ")))
add, sub, mul, div = map(int, input().split())

ans_max=-100000
ans_min =100000
# 각 하나의 노드에 operations의 연산들을 각각할 수 있다
# 각 노드의 순서는 정해져있다
# 이때 , 연산의 순서는 상관없다 그렇기 때문에 모든 경우의 수를 고려해줘야한다
#



def dfs(i, res, add, sub, mul, div):
    global  ans_max
    global  ans_min
    if i ==n:
        ans_max = max(ans_max, res)
        ans_min = min(ans_min,res)
        return
    else:
        if add :
            dfs(i+1, res+testcase[i], add-1, sub,mul,div)
        if sub :
            dfs(i+1, res- testcase[i],add, sub-1,mul,div)
        if mul :
            dfs(i+1, res*testcase[i],add,sub,mul-1,div)
        if div :
            dfs(i+1, int(res/testcase[i]),add,sub,mul,div-1)


dfs(1, testcase[0], add, sub, mul, div)
print(ans_max)
print(ans_min)