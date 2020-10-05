n=int(input())
student=[]
for i in range(n):
    height,weight=input().split(" ")
    student.append((int(height),int(weight)))


def solve():
    ans = ""
    for i in range(len(student)):
        rank = 1
        w = student[i][0]
        h = student[i][1]
        for j in range(len(student)):
            if w < student[j][0] and h < student[j][1]:
                rank += 1
        ans+=str(rank)+" "
    return ans

print(solve())