
def convertnumber(word):
    if word=="Z":
        return 10
    conver_number=(ord(word)-65)//3+3
    return conver_number

w=input()
number=[]
for i in range(len(w)):
    number.append(int(convertnumber(w[i])))

print(sum(number))

