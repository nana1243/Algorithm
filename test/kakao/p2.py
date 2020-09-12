# 시간초과 -3, 나머지 통과

from itertools import combinations
def solution(orders, course):
    menus = set()
    information = { "guest"+str(i+1) : list(orders[i]) for i in range(len(orders))}

    for value in information.values():
        for menu in value:
            menus.add(menu)

    start=0
    ans=[]
    max_course =max(course)

    while start <=len(course)-1:
        combination_menu =list(combinations(menus,course[start]))
        d_course={}
        d_description={}

        for idx,elm in enumerate(combination_menu):
            course_id = "courseid_"+str(idx+1)
            values  = list(elm)
            d_course[course_id]=values
            d_description[course_id]=0



        for course_idx in d_course :
            setB = set(d_course[course_idx])
            for info_idx in range(len(information)):
                setA =set(information["guest"+str(info_idx+1)])
                if setA.intersection(setB)==setB:
                    d_description[course_idx]+=1


        max_combination=max(d_description.values())

        for key in d_description:
            if d_description[key]==max_combination and max_combination>=2 :
                res = ''.join(e for e in d_course[key])
                ans.append(res)

        start+=1

    ans.sort()

    return ans