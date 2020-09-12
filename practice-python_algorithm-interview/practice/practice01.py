# 매일매일 공부하기

testcase=[1,2,3]

result_permutaion_dfs=[]
prev_element=[]

def permutaion_dfs(testcase):
    if len(testcase)==0:
        result_permutaion_dfs.append(prev_element[:])

    for elm in testcase:
        next_element = testcase[:]
        next_element.remove(elm)

        prev_element.append(elm)
        permutaion_dfs(next_element)
        prev_element.pop()



permutaion_dfs(testcase)
print(result_permutaion_dfs)




result_combination_dfs=[]
def combination_dfs(element,start,k):
    if k==0:
        result_combination_dfs.append(element[:])

    for i in range(start,5):
        element.append(i)
        combination_dfs(element,i+1,k-1)
        element.pop()


combination_dfs([],1,2)
print(result_combination_dfs)


