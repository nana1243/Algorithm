# trie의 높이가 작은집합을 큰집합과 합친다


class DisjointSet:
    def __init__(self,n):
        self.data = [-1 for _ in range(n)]
        self.size = n

    # 그룹이 존재하고 그에 따른 조상이 존재하면 그 조상의 번호를 return 해라
    # 만약 그렇지 않다면 (그룹이 없다면) 해당되는 index를 출력해라
    def find(self,index):
        value = self.data[index]
        if value<0:
            return index
        return self.data[index]   
    
    # height가 작은 것이 큰것과 합쳐진다
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x==y:
            return

        if self.data[x]<self.data[y]:
            self.data[y]=x

        elif self.data[x]>self.data[y]:
            self.data[x]=y
        else:
            self.data[x]-=1
            self.data[y]=x

       

disjoint = DisjointSet(10)

print(disjoint.data)
disjoint.union(1,2)
print(disjoint.data)
disjoint.union(2,3)
print(disjoint.data)



        





