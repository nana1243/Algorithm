def solution(clothes):
    from collections import Counter
    from functools import reduce
        
    clothes_number=Counter(element[1] for element in clothes)
    
    answer=reduce(lambda x,y: x*(y+1), clothes_number.values(),1)-1
    return answer