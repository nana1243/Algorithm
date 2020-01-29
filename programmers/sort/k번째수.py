def solution(array, commands):
    answer=[]
    for i in range(len(commands)):
        if commands[i][1] > len(array):
            answer_array=array[commands[i][1]-1:commands[i][-1]]
        elif commands[i][0]<0:
            answer_array = array[commands[i][0]:commands[i][-1]]
        else:
            answer_array=array[commands[i][0]-1:commands[i][1]]
        answer_array.sort()
        answer.append(answer_array[commands[i][2]-1])

    return answer