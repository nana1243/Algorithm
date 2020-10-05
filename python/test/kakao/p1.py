



class Rule:
    def __init__(self,new_id):
        self.new_id = new_id

    def rule1(self):
        self.new_id = self.new_id.lower()

    def rule2(self):
        new_id = self.new_id
        result = ""
        for idx, elm in enumerate(new_id):
            if elm.isalnum():
                result += elm
            else:
                if elm == "-" or elm == "_" or elm == ".":
                    result += elm

        self.new_id = result

    def rule3(self):
        new_id = self.new_id
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
        self.new_id= result

    def rule4(self):
        new_id = self.new_id
        if new_id.startswith("."):
            new_id = new_id[1:]
        if new_id.endswith("."):
            new_id = new_id[:-1]
        self.new_id = new_id

    def rule5(self):
        if len(self.new_id) == 0:
            self.new_id="a"

    def rule6(self):
        new_id = self.new_id
        if len(new_id) >= 16:
            new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        self.new_id = new_id

    def rule7(self):
        if len(self.new_id) <= 2:
            input_string = self.new_id[-1]
            while len(self.new_id) < 3:
                self.new_id += input_string




def solution(new_id):
    user = Rule(new_id)
    user.rule1()
    user.rule2()
    user.rule3()
    user.rule4()
    user.rule5()
    user.rule6()
    user.rule7()
    return user.new_id




print(solution("abcdefghijklmn.p"))
print(solution("."))


