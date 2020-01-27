### DFS BFS

#### 1.DFS 와 BFS의 기본형태 > 둘의 가장 큰 차이점은 스택(DFS)를 쓰냐 , 큐(BFS)를 쓰냐이다

1. DFS

   ```python
   def dfs():
       d_visit = []
       stack = [V]
       d_check = [0 for _ in range(N+1)]
       while stack:
           v1 = stack.pop()
           if not d_check[v1]:
               d_check[v1] = 1
               d_visit.append(v1)
               stack += edge[v1]
       return d_visit
   
   ```

2. BFS

   ```python
   def bfs():
       b_visit = []
       queue = [V]
       b_check = [0 for _ in range(N+1)]
       b_check[V] = 1
       while queue:
           v2 = queue.pop()
           b_visit.append(v2)
           for i in reversed(edge[v2]):
               if not b_check[i]:
                   b_check[i] = 1
                   queue = [i] + queue
       return b_visit
   
   print(' '.join(map(str,bfs())))
   ```

## 문제 유형

> 1. 일반 dfs,bfs 문제
> 2. 몇개의 그룹이 있는지 
> 3. 최소 거리(BFS) - 가중치가 없는 경우
> 4. 이차원
> 5.  트리형



### 1.일반적 DFS/BFS문제 + 그룹안의 원소갯수세기

#### 1-1 BOJ 2260 바이러스



## 문제

신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

![img](https://www.acmicpc.net/upload/images/zmMEZZ8ioN6rhCdHmcIT4a7.png)

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

## 출력

1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

## 예제 입력 1 복사

```
7
6
1 2
2 3
1 5
5 2
5 6
4 7
```

## 예제 출력 1 복사

```
4
```



풀이

```python
N=int(input())
M=int(input())
edge=[[]for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)


def bfs():
    bcheck=[0 for i in range(N+1)]
    banswer=[]
    q=[1]
    bcheck[1]=1
    while q:
        p=q.pop()
        banswer.append(p)
        for e in edge[p]:
            if bcheck[e]==0:
                bcheck[e]=1
                q.append(e)
    return len(banswer)-1

print(bfs())


```





## 2. 2차원문제



## 문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

![img](https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png)

## 입력

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

## 출력

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

## 예제 입력 1 복사

```
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```

## 예제 출력 1 복사

```
3
7
8
9
```



솔루션

```python 
M=7
import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

matrix = [list(map(int, list(read()))) for _ in range(n)]


def dfs(matrix, cnt, x,y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 하고 0으로 바꾸는것 이다.
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if n_x>=0 and n_x<n and n_y>=0 and n_y<n:
            if matrix[n_x][n_y]==1:
                cnt = dfs(matrix, cnt+1, n_x, n_y)
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            ans.append(dfs(matrix, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)


```







## 3. 최소거리문제

### 3-2 이차원문제

```python
def bfs(x,y,cnt):
    q.append((x,y))
    check[y][x] = 1
    answer[y][x] = cnt
    while q:
        x,y=q.popleft()
        # if nx !=x and ny !=y:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and ny>=0 and nx<X and ny<Y:
                if check[ny][nx]==0 and matrix[ny][nx]==1:
                    check[ny][nx]=1
                    answer[ny][nx]=answer[y][x]+1
                    q.append((nx,ny))


    return answer
from pprint import pprint
pprint(bfs(0,0,cnt)[Y-1][X-1]+1)


```

여기서 주목해야 할 부분은

```python
answer[ny][nx]=answer[y][x]+1
```



3-2 일차원 최소거리

프로그래머스 단어변환 문제

https://programmers.co.kr/learn/courses/30/lessons/43163

```python
def solution(begin, target, words):
    # target의  문자가 없을 경우
    if target not in words:
        return 0

    end = words.index(target) + 1
    # edge 그래프 형성
    edge = [[] for i in range(len(words) + 1)]
    from collections import Counter
    for i in range(len(words)):
        if len(Counter(begin) - Counter(words[i])) == 1:
            edge[0].append(i + 1)

    if len(edge) == 0:
        return 0

    for i in range(len(words)):
        for j in range(len(words)):
            if len(Counter(words[i]) - Counter(words[j])) == 1:
                if j + 1 not in edge[i + 1]:
                    edge[i + 1].append(j + 1)
                if i + 1 not in edge[j + 1]:
                    edge[j + 1].append(i + 1)

    #################### edge 그래프형성 끝 ######################

    from collections import deque
    q = deque()
    check = [0 for i in range(len(words) + 1)]
    visit = []

    def bfs(start):
        layer = {start: 1}
        check[start] = 1
        q.append(start)
        while q:
            p = q.popleft()
            for e in edge[p]:
                if check[e] == 0:
                    check[e] = 1
                    layer[e] = layer[p] + 1
                    q.append(e)
        return layer[end]

    answer = []
    for i in range(len(edge[0])):
        answer.append(bfs(edge[0][i]))

    return min(answer)


```



여기서 중요한 표현

```python
layer[e] = layer[p] + 1
```





### 4 그룹의 수 세기

4-1.BOJ 유기농양배추



```python

# testnumber=int(input())
X,Y,T=10,8,17
# N은 가로길이 , M은 세로길이
import pprint
matrix=[[0 for _ in range(X)] for i in range(Y)]

for i in range(T):
    a,b=map(int,input().split())
    matrix[b][a]=1

cnt=0
def dfs(x,y,matrix):
    matrix[y][x]=0
    dx = [1, -1, 0, 0]
    dy = [0, -0, 1, -1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<X and ny>=0 and ny<Y:
            if matrix[ny][nx]==1:
                dfs(nx,ny,matrix)
    return

cnt=0
for i in range(X):
    for j in range(Y):
        if matrix[j][i]==1:
            dfs(i,j,matrix)
            cnt+=1
print(cnt)

```

% 여기서 중요한 표현%

- 그룹의 수를 세기 위한 표현

```python
for i in range(X):
    for j in range(Y):
        if matrix[j][i]==1:
            dfs(i,j,matrix)
            cnt+=1
print(cnt)

```









