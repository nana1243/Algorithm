# 책이랑 다르게 코딩 (아이디어는 유사)

nums=[3,4,5,6,7,8,9,10,0,1,2]
target = 1

# 회전되기전의 가장 첫 스타트점을 찾는다

# num[left]>num[mid] and num[mid]<num[right] 인지점을 찾아야 한다


def search(nums:list):
    left =0
    right = len(nums)-1

    while left<right:
        mid=(left+right)//2

        if nums[left]<nums[mid]:
            left=mid-1

        elif nums[mid]>nums[right]:
            right=mid+1
        else:
            left=mid
            right=mid

    return mid


print(search(nums))