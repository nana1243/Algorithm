

# 높이를 입력받아 비 온후 얼마나 많은 물이 쌓일 수 있는 지 계산

t = [0,1,0,2,1,0,1,3,2,1,2,1]


# 포인터를 활용하여 문제 풀이

def sol1(height:list[int]):
    if not height :
        return 0

    volume =0
    left, right =0,len(height)-1

    while left<right :
        left_max , right_max = max(height[left],left_max), max(height[right],right)

        # 더 높은 쪽을 향해 포인터들이 이동

        if left_max <= right_max:
            volume+=left_max -height[left]





    # 양쪽의 최대를 찾아라

