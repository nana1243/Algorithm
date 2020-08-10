# 괄호로 된 입력값이 올바른지 판단하세요

testcase = "()[]{}"

# 풀이 1

stack=[]
table ={
    ")" : "(" ,
    "}" : "{" ,
    "]" :"["
}

def sol1(testcase):
    for char in testcase:
        if char not in table:
            stack.append(char)
        elif not stack or table[char]!=stack.pop():
            return False

    return len(stack)==0

