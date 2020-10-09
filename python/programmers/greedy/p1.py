def solution(n, lost, reserve):
    student = {i + 1: 1 for i in range(n)}
    for i in range(len(lost)):
        student[lost[i]] -= 1
    for i in range(len(reserve)):
        student[reserve[i]] += 1
    for i in range(1, n + 1):
        if i == 1:
            if student[i] == 0 and student[i + 1] > 1:
                student[i] += 1
                student[i + 1] -= 1
        elif 1 < i < n:
            if student[i] == 0 and student[i + 1] > 1:
                student[i] += 1
                student[i + 1] -= 1
            elif student[i] == 0 and student[i - 1] > 1:
                student[i] += 1
                student[i - 1] -= 1
        elif i == n:
            if student[i] == 0 and student[i - 1] > 1:
                student[i - 1] -= 1
                student[i] += 1

    answer = list(filter(lambda x: x >= 1, student.values()))
    return len(answer)