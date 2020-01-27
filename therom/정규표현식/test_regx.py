import datetime
import re

x = datetime.datetime(2020, 5, 17)
print(x)
# 요일 중 wed만 출력
print(x.strftime("%a"))
print(x.strftime("%A"))


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


txt = "The rain in spain"
x = re.search("[a-f]", txt)
print(x.span())
print(x.end())


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


import re

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)


import re

txt = "i am java hello world"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
print(x)


for i in list(txt.split(" ")):
    print(i.startswith("hello"))



import re

txt = "The xraixn in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)
print(x)