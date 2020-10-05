

# while(true){a,b=map(int,input().split())
#     print(a+b)}

while True:
    a,b=input().split(" ")
    if a=="\n" or b=="\n":
        break
    else:
        print(int(a)+int(b))

