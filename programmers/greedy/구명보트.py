def solution(people, limit):
    people.sort()
    light=0
    heavy=len(people)-1
    answer=0
    while lsight<heavy:
        if people[light]+people[heavy]<=limit:
            light+=1
            heavy-=1
            answer+=1
        else:
            heavy-=1
        
    return len(people)-answer