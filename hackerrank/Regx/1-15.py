## 문제 :Task
# You have a test string . Your task is to match the string hackerrank. This is case sensitive.



#####2번 ################
Regex_Pattern = r"\d\d"	# Do not elete 'r'.

# import re
# print(re.findall(Regex_Pattern,input()))


###########3번######### 공백 탭 등과 같은 whitespace와 매칭
# Regex_Pattern = r"\S\S\s\S\S\s\S\S"
# import re
# print(re.findall(Regex_Pattern,input()))


# Matching Word & Non-Word Character
# 글자인것 : \w
# 글자가 아닌것 : \W
# Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"
# import re
# print(re.findall(Regex_Pattern,input()))




import re
txt="""
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
"""

rex=r'<[\w\/\.\w]*>'
import re
answer=[]
rex=r'<\w+'
for element in (re.findall(rex,txt)):
    result=re.sub("<","",element)
    answer.append(result)

answer=list(set(answer))
answer.sort()
answer=";".join(item for item in answer)

print(answer)

# p1=r'(/\*.*?/|//.*?$)'
p1 = r'(/\*.?*\*/|//.{0,})'

txt="""
// my  program in C++
#include <iostream>
/** playing around in
a new programming language **/
using namespace std;
int main ()
{
  cout << "Hello World";
  cout << "I'm a C++ program"; //use cout
  return 0;
}
"""
a=re.findall(p1,txt)
answer="\n".join(element for element in a)
print(answer)