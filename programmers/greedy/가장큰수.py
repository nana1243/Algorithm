number="10000"
k=1
target_long=len(number)-k
first =0
answer =""
long=len(number)
def result(number ,k ,answer ,long):
    first = 0
    input = max(number[first:k+1])
    first = number.index(input)
    answer +=str(input)
    long-=1
    k-= first
    number=number[first+1:]
    if k==0:
        answer+=number
        return answer
    if target_long==len(answer):
        return answer
    return result(number, k ,answer ,long)


print(result(number, k  ,answer ,long))
