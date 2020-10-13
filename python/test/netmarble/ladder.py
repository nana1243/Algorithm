# 사다리문제 복기

def move(start):
    arr= [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]]
    x = start-1
    y = 0
    h = len(arr)
    l = len(arr[0])

    while y<h:
        if x>=1 and arr[y][x-1]==1 :
            arr[y][x-1] = 0
            x-=1

        elif x<l and arr[y][x] ==1:
            arr[y][x] = 0
            x+=1

        else:
            y+=1

    return x+1,y



ans1 = move(start =1)
print(ans1)
ans2 = move(start =2)
print(ans2)
ans3 = move(start =3)
print(ans3)
ans4= move(start=4)
print(ans4)


