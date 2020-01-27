### 최소신장트리

#### 최소신장트리?

- 신장트리란, 사이클을 형성하지 않고 그래프의 모든 정점(V)이 간선(E)으로 연결되어 있는 것
- 최소신장트리란 최소한의 비용으로 신장트리를 형성하는 것



#### Kruskal's Algorithm

- 모든 정점을 독립적인 집합으로 만든다.
- 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
- 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.
- 시간 복잡도는 0(Elog(V))

```python
parent = {}
rank = {}

# 정점을 독립적인 집합으로 만든다.
def make_set(v):
    parent[v] = v
    rank[v] = 0

# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        
    return parent[v]

# 두 정점을 연결한다.
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1
​
def kruskal(graph):    
    for v in graph['vertices']:
        make_set(v)
    
    mst = []
    
    edges = graph['edges']
    edges.sort()
    
    for edge in edges:
        weight, v, u = edge
                
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    
    return mst
            

```





1-1 find , union 함수

##### union-find

##### disjoint-set algorithm : 구체적으로 여러 개의 노드가 존재할 때 두 개의 노드를 선택해서, 현재 이 두 노드가 서로 같은 그래프에 속하는지 판별하는 알고리즘



```python
class DisjointSet():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = n

    def find(self, idx):
        while idx != self.parent[idx]: idx = self.parent[idx]
        return idx

    def union(self, a, b):
        #a, b를 입력 받았을 때 a를 기준으로 합한다!
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
            self.rank[b] += 1
        else:
            self.parent[b] = a
            self.rank[a] += 1


n, m = map(int, input().split())
obj = DisjointSet(n + 1)
for _ in range(m):
    f, a, b = map(int, input().split())
    if f==1:
        #a와 b가 같은 집합인지 확인.
        print("YES" if obj.find(a) == obj.find(b) else "NO")
    else:
        #a와 b를 합
        obj.union(a, b)
```



