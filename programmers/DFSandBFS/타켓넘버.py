# 문제 설명
# n개의 음이 아닌 정수가 있습니다.
# 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3


####################coding start ####################

numbers=[1, 1, 1, 1, 1]
target=3
##5 라는 값이 나온다

def operator(numbers,idx,cnt):
    if idx<len(numbers):
        numbers[idx] *=1
        print("first",numbers)
        operator(numbers,idx+1,cnt)

        numbers[idx] *=-1
        print("second",numbers)
        operator(numbers,idx+1,cnt)

    elif sum(numbers)==target:
        cnt+=1
    return cnt

print(operator(numbers,idx=0,cnt=0))