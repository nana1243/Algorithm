
# 모두통과

def rule1(new_id):
    return new_id.lower()


def rule2(new_id):
    result = ""
    for idx, elm in enumerate(new_id):
        if elm.isalnum():
            result += elm
        else:
            if elm == "-" or elm == "_" or elm == ".":
                result += elm
    return result


def rule3(new_id):
    result = ""
    start = 0
    while start <= len(new_id) - 1:
        for i in range(start, len(new_id)):
            result += new_id[i]
            start = i + 1
            if new_id[i] == ".":
                for j in range(i + 1, len(new_id)):
                    start = j
                    if new_id[j] != ".":
                        break
                break

    return result


def rule4(new_id):
    if new_id.startswith("."):
        new_id = new_id[1:]
    if new_id.endswith("."):
        new_id = new_id[:-1]
    return new_id


def rule5(new_id):
    if len(new_id) == 0:
        return "a"
    return new_id


def rule6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    return new_id


def rule7(new_id):
    if len(new_id) <= 2:
        input_string = new_id[-1]
        while len(new_id) < 3:
            new_id += input_string
    return new_id


def solution(new_id):
    new_id = rule1(new_id)
    new_id = rule2(new_id)
    new_id = rule3(new_id)
    new_id = rule4(new_id)
    new_id = rule5(new_id)
    new_id = rule6(new_id)
    new_id = rule7(new_id)
    return new_id


print(len("abcdefghijklmn.p"))
print(solution("abcdefghijklmn.p"))



