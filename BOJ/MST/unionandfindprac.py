# class disjoint의 초기조건
class DisjointSet:
    def __init__(self,n):
        # class가 생성되자마자 n의 크기인 리스트가 만들어진다
        self.data = list(range(n))
        self.size = n
    
    # 리스트의 idx의 값을 반환해준다
    # 이 함수의 역할은 같은 집합인지를 찾아주는 역할이다
    def find(self,index):
        return self.data[index]
    
    # x,y와 같은 합집합으로 만들어준다
    # y의 조상은 x로 바꾸어준다
    # 그리고 y에연결된 자손들을 x의 자손으로 바꾸어준다

    def union(self,x,y):
        x,y = self.find(x),self.find(y)
        if x==y:
            return 
        
        for i in range(self.size):
            if self.find(i) ==y:
                self.data[i] = x
    
    def length(self):
        long = len(set(self.data))
        return long

    def __repr__(self):
        return str(self.data)





disjoint = DisjointSet(6)

# 5의 조상은 1로 바꾸어준다
# disjoint.union(1,5)
# print(disjoint.data)
# # 5의 조상은2로 바꾸어준다
# # 이때 5의 식구들도 모두 조상을 2로 바꾸어준다
# disjoint.union(2,5)
# print(disjoint.data)

disjoint.union(2,3)    
print(disjoint.data)
disjoint.union(1,2)
print(disjoint.data)

