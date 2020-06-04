#### backtracking의 문제 해결방법####
"""
주요 개념은 해를 얻을 때까지 모든 가능성을 시도한다는 점이다. 모든 가능성은 하나의 트리처럼 구성할 수 있으며, 가지 중에 해결책이 있다.
트리를 검사하기 위해 깊이 우선 탐색을 사용한다. 탐색 중에 오답을 만나면 이전 분기점으로 돌아간다.
시도해보지 않은 다른 해결 방법이 있으면 시도한다. 해결 방법이 더 없으면 더 이전의 분기점으로 돌아간다.
모든 트리의 노드를 검사해도 답을 못 찾을 경우, 이 문제의 해결책은 없는 것이다.
"""


## 1. n-queen문제 ####

# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

n=8
height,digonal,inverse_digonal =[False]*n, [False]*(2*n-1), [False]*(2*n-1)

ans=0
def solve(i):
    global ans
    if i==n:
        ans+=1
        return
    for j in range(n):
        if not(height[j] or digonal[i+j] or inverse_digonal[i-j+n-1]):
            height[j] = digonal[i + j] = inverse_digonal[i - j + n - 1] = True
            solve(i+1)
            height[j] = digonal[i + j] = inverse_digonal[i - j + n - 1] = False

solve(0)
print(ans)

#######2. 스도쿠문제





## 1.