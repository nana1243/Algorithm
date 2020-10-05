import sys

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, sys.stdin.readline().split())))

def greedy(meeting):
    cnt=1
    start=meeting[0][0]
    end=meeting[0][1]
    for i in range(1,len(meeting)):
        if end<=meeting[i][0] :
            start=meeting[i][0]
            end=meeting[i][1]
            cnt+=1
    return cnt


# 빨리 끝나는순 빨리 끝난다면 시간이 빠른 순서
meeting = sorted(meeting, key=lambda x: (x[1],x[0]))
ans1= greedy(meeting)

meeting = sorted(meeting, key=lambda x: (x[0],x[1]))
ans2= greedy(meeting)

ans= max(ans1,ans2)

print(ans)