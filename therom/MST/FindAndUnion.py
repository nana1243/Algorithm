
######### find and union ################


### 가장 먼저 find의 함수의 역할은 ?
### find(a) 했을때 a의 최고 조상을 찾는 것이다

n=5
p=[i for i in range(n)]

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

# v를 u의 자손으로 병합시키는 함수
def union(u,v):
    root1 = find(u)
    root2 = find(v)
    p[root2] =root1


######################################### 클래스로 공부######################################



class DisjointSet:
    def __init__(self,n):
        self.data =[i for i in range(n)]
        self.size = n

    def find(self,u):
        if self.data[u] !=u:
            return self.data[self.data[u]]
        return self.data[u]

    def union(self,u,v):
        u,v = self.find(u), self.find(v)
        if u==v:
            return
        for i in range(self.size):
            if self.find(i) == v:
                self.data[i] = u


d = DisjointSet(5)
d.union(0,1)
d.union(1,2)
d.union(3,4)
print(d.data)

##########################  trie형태로####################

## 작은 갯수의 트리가 큰 트리로 병합한다


class disjointTrie:
    def __init__(self,n):
        self.data = [-1 for _ in range(n)]
        self.size = n

    def find(self,index):
        value = self.data[index]
        # 최고조상일때
        if value<0:
            return index
        return self.data[value]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] > self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x


d2= disjointTrie(7)
d2.union(0,1)
d2.union(0,3)
d2.union(2,4)
d2.union(2,6)
d2.union(2,5)

print(d2.data)