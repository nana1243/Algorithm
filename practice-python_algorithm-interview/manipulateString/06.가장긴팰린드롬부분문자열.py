
test="babad"


def expand(left:int, right:int, word:list):
    while left>=0 and right<=len(word)-1 and word[left]==word[right]:
        left-=1
        right+=1
    return word[left:right+1]

def longestPalidrome(word:str):

    if len(word)<2 or word==word[::-1]:
        return True
    result=[]

    for i in range(len(word)):
        result = max(result,expand(i,i+1),key=len)


    return result



print(longestPalidrome(test))