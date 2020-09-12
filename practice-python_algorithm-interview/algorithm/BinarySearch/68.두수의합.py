# 정렬된 배열에서 덧셈하여 target을 만들 수 있는
# 두숫자의 인덱스를 리턴하여라


numbers=[2,7,11,15,18,20,29,31]

target=31


def makeTarget_twopoint(numbers,target):

    left=0
    right=len(numbers)-1

    while left!=right:
        if numbers[left] + numbers[right]>target:
            right-=1
        elif numbers[left] +  numbers[right]<target:
            left-=1

        else:
            return [left,right]
print(makeTarget_twopoint(numbers,target))
#
def makeTarget(numbers,target):

    for idx,elm in enumerate(numbers):
        left=idx+1
        right=len(numbers)-1

        while left<=right:
            mid = (left +right )//2
            if elm + numbers[mid]> target:
                right=mid-1
            elif elm +numbers[mid]< target:
                left=mid+1
            else:
                return [idx,mid]


print(makeTarget(numbers,target))