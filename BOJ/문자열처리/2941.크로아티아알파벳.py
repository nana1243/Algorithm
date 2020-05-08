croatia=["c=","c-","dz=","d-","lj","nj","s=","z="]

test=input()

for i in croatia:
    test=test.replace(i,"0")

print(len(test))