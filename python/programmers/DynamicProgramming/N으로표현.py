def cal(x, y):
    plus = x + y
    minus = x - y
    multi = x * y
    try:
        div = x // y
    except ZeroDivisionError:
        div=0
    return [plus, minus, multi, div]

result = [ [5], [ 5+ 5, 5-5, 5* 5, 5 // 5]]
cnt = 2
number=12


while cnt<8:
    input = []
    for i in range(len(result[cnt-1])):
        for j in range(len(result[cnt-2])):
            input.append(cal(result[cnt-2][j],result[cnt-1][i]))
    result.append(input)
    if number in result[cnt] :
        print(cnt)
        break
    else:
        cnt+=1

