# 2. 각 지원자들의 그룹은 reject안에 있는 지원자로 시작한다
from heapq import heappush
from heapq import heappop
from collections import defaultdict

def solution(companies, applicants):
    company_information = defaultdict()
    applicant_information = defaultdict()


    for company in companies:
        company = company.split(" ")
        company_information[company[0]] = {"name" : company[0],"total": int(company[2]), "prefer": list(reversed(company[1]))}


    for applicant in applicants:
        applicant = applicant.split(" ")
        applicant_information[applicant[0]]= {"name": applicant[0], "total": applicant[2], "prefer": applicant[1][:int(applicant[2])]}

    reject = [elm for elm in applicant_information ]


    # while reject:
    # 1. 각 지원자가 회사선택
    # 1-1 if 회사채용인원 꽉 찼으면 = > reject 안에 넣는다(이때 , 고려해야함)
    # 1-2 elif 회사채용인원 꽉 안찼으면 => {회사명:[]}이런 형태로 넣는다
    # 1-3 지원자가 지원가능한 회사 목록을 지운다
    # 1-4 reject reset




    match_success ={company_name:[]  for company_name in company_information }


    while reject:
        tmp=[]
        for applicant in reject:
            infomation = applicant_information[applicant]
            apply_company = infomation["prefer"][0]
            applicant_information[applicant]["prefer"] = applicant_information[applicant]["prefer"][1:] #지원한 회사 지운다

            heappush(match_success[apply_company],[ company_information[apply_company]["prefer"].index(applicant) ,applicant] )  # 우선순위, 지원자 이름을 넣는다

            if len(match_success[apply_company]) > company_information[apply_company]["total"]: # 정원이 넘으면
                rejected_people_index,rejected_people = heappop(match_success[apply_company])
                if  applicant_information[rejected_people]["prefer"] !="":
                    tmp.append(rejected_people)
        reject = tmp[::]

    # ans가공

    #1. sort한다
    #2. 기업명_지원자 형태로 가공한다
    ans =[elm+"_" for elm in match_success]

    for idx,key in enumerate(match_success):
        match_success[key].sort(key = lambda x:x[1])
        for elm in match_success[key]:
            ans[idx]+=elm[1]

    print(ans)
    return



ans1=solution(companies= ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"],applicants=["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"] )

ans2=solution(companies=["A abc 2", "B abc 1"], applicants=	["a AB 1", "b AB 1", "c AB 1"])
print(ans1)