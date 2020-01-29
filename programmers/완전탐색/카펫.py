def solution(brown, red):
    # red의 약수를 구한다 [a,b]
    # brown+red의 약수를 구한다[a+2,b+2] 가 존재한다면 출력
    def solve_red(red):
        red_list=[]
        for i in range(1,red+1):
            if red%i==0:
                red_list.append(i)
        return red_list
    red_list=solve_red(red)
    S=brown+red
    for element_one in red_list:
        for element_two in red_list:
            if (element_one+2)*(element_two+2)==S:
                if element_one<=element_two:
                    return [element_two+2,element_one+2]
                else:
                    return [element_one+2,element_two+2]