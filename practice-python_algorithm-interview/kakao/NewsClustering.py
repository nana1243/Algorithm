from collections import Counter


def parsing(string):
    strlist = []
    string = string.lower()
    for i in range(len(string) - 1):
        tmp = string[i:i + 2]
        strlist.append(tmp[::])
    strlist = list(filter(lambda x: x.isalpha() == True, strlist))
    return strlist


def jacard(s3: list, s4: list):
    diff_a = Counter(s3) - Counter(s4)
    intersection = (Counter(s3) - diff_a)
    union = (Counter(s3) + Counter(s4)) - intersection
    ans = 65536

    if len(union) == 0:
        return ans
    denominator = sum(elm for elm in union.values())
    numerator = sum(elm for elm in intersection.values())
    ans = int((numerator / denominator) * ans)

    return ans


def solution(str3, str4):
    s3, s4 = parsing(str3), parsing(str4)
    ans = jacard(s3, s4)

    return ans