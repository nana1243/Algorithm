# def solution(people, limit):
#     people.sort()
#     ans=0
#     while(len(people)>=1):
#         w=0
#         for i in range(len(people)):
#             if w+people[i]>limit:
#                 print(people[i:])
#                 people=people[i:]
#                 break
#             else:
#                 w+=people[i]
#         ans+=1
#     print(ans)
    
# solution(people=[70, 50, 80, 50],limit=100)




