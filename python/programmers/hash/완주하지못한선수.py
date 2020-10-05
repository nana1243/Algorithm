def solution(participant, completion):
    from collections import Counter
    
    participant_counter=Counter(participant)
    completion_counter=Counter(completion)
    diff=participant_counter-completion_counter
    answer=list(diff)[0]
    return answer