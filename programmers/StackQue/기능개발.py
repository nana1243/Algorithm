def solution(progresses, speeds):    
    import collections
    import math
    def complete():
        c=[]
        for i in range(len(progresses)):
            result=(100-progresses[i])/speeds[i]
            result=math.ceil(result)
            c.append(result)
        return c
    c=complete()
    for i in range(0,len(c)-1):
        if c[i]>c[i+1]:
            c[i+1]=c[i]
        else:
            pass    
    
    answer=collections.Counter(c)
    answer=list(answer.values())
    
    return answer