from collections import Counter

# 정확성 100, 효율성all 통과못함
def infoParsing(information, query):
    information = information.split(" ")
    language = information[0].strip()
    job = information[1].strip()
    career = information[2].strip()
    soulfood = information[3].strip()
    score = int(information[4].strip())
    d = {"language": language, "job": job, "career": career, "soulfood": soulfood, "score": score}
    for elm in query:
        if query[elm] == "-":
            d[elm] = "-"
    return d


def queryParsing(query):
    query = query.split("and")
    language = query[0].strip()
    job = query[1].strip()
    career = query[2].strip()
    idx = 0
    for i in range(len(query[3])):
        if query[3][i].isdigit():
            idx = i
            break
    soulfood = query[3][:idx].strip()
    score = int(query[3][idx:].strip())
    d = {"language": language, "job": job, "career": career, "soulfood": soulfood, "score": score}

    return d



def solution(info, query):
    d_query = {"query_" + str(i): 0 for i in range(len(query))}

    for idx, element in enumerate(query):
        key = "query_" + str(idx)
        queryparsing = queryParsing(element)
        d_query[key] = queryparsing

    start = 0
    ans=[]

    while start < len(d_query):
        d_info = {"applicant_" + str(i): 0 for i in range(len(info))}
        need = d_query["query_" + str(start)]

        for idx, element in enumerate(info):
            key = "applicant_" + str(idx)
            infoparsing = infoParsing(element, need)
            d_info[key] = infoparsing

        cnt=0
        query_value = list(need.values())

        for element in d_info:
            compare =list(d_info[element].values())
            if compare[:-1]== query_value[:-1]:
                if compare[-1]>=query_value[-1]:
                    cnt+=1

        ans.append(cnt)
        start += 1

    return ans





info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"]

solution(info,query)
