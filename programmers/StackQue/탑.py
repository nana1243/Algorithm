heights=[1,5,3,6,7,6,5]
answer = [0 for i in range(len(heights))]
idx = len(heights)-1

while idx>0:
    for i in range(idx-1,-1,-1):
        if heights[idx]<heights[i]:
            answer[idx]=i+1
            break
    idx-=1



print(answer)