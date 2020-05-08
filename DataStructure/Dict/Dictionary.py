# 번호를 key로 갖고 이름을 value로 가지는 dictionary 만들기
students = ['몽키', '선샤인', '시와', '톰']
for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다'.format(number+1, name))

# Dictionary Comprehension
students_dic = {
    '{}번'.format(number+1) : name for number, name in enumerate(students)
}

print(students_dic)




students = ['몽키', '선샤인', '시와', '톰']
scores = [85, 92, 78, 100]

for x, y in zip(students, scores):
    print(x, y)

 ### 딕셔너리에서 zip
score_dic = {
    student : score for student, score in zip(students, scores)
}

print(score_dic.get("몽키"))
print(score_dic.get("시와"))

#튜플형태로 출력
print(list(score_dic.items()))

