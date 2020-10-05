n=int(input())

for i in range(n):
    number,test=input().split()
    number=int(number)
    answer=""
    for j in range(len(test)):
        answer+=test[j]*number
    print(answer)