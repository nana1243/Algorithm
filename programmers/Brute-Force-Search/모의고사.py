def solution(answers):
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    def is_it_solution(answers:list, people:list):
        count=0
        for i in range(len(answers)):     
            if answers[i]==people[i% len(people)]:
                count+=1
            else:
                count+=0
        return count
        
        
    answer=[]    
    def for_return_answer():
        a=[is_it_solution(answers,one),is_it_solution(answers,two),is_it_solution(answers,three)]
        for i in range(len(a)):
            if a[i]==max(a):
                answer.append(i+1)
            else:
                pass
        return answer
    
    for_return_answer()
    return answer