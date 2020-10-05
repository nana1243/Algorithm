


n = int(input())
d = [[0]*3 for _ in range(n+1)]

p = [[0]*3]+[list(map(int, input().split())) for _ in range(n)]
print(p)

def solve():
    #p[1][i] 시작점에 따라 달라진다
    for i in range(3):
        d[1][i] = p[1][i]
    for i in range(2, n+1):
        # 같은 색이 되서는 안된다
        d[i][0] = min(d[i-1][1], d[i-1][2]) + p[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + p[i][1]
        d[i][2] = min(d[i-1][0], d[i-1][1]) + p[i][2]
    return min(d[n])

solve()


