### Regx Functions

| Function                                                     | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [findall](https://www.w3schools.com/python/python_regex.asp#findall) | Returns a list containing all matches                        |
| [search](https://www.w3schools.com/python/python_regex.asp#search) | Returns a [Match object](https://www.w3schools.com/python/python_regex.asp#matchobject) if there is a match anywhere in the string |
| [split](https://www.w3schools.com/python/python_regex.asp#split) | Returns a list where the string has been split at each match |
| [sub](https://www.w3schools.com/python/python_regex.asp#sub) | Replaces one or many matches with a string                   |
| match                                                        |                                                              |



1. findall : 찾으려는 문구가 리스트 형식으로 출력됨
   - 이때 ,찾으려는 txt안에 없을 경우 : 빈리스트가 출력된다

```python
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) 

```



2. search

   > The `search()` function searches the string for a match, and returns a [Match object](https://www.w3schools.com/python/python_regex.asp#matchobject) if there is a match.
   >
   > If there is more than one match, only the first occurrence of the match will be returned:
   >
   > = 더많은 match가 있더라도 , 오직 한개만 추출 된다

   

   ```python
   
   txt = "The rain in spain"
   x = re.search("[a-f]", txt)
   print(x.span())
   print(x.end())
   
   ```

   

3. Split 
   
   - 기준으로 나눈다

```python
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
```

3-1 maxsplit

- 몇개로 나눌 수 있을지도 정할 수 있다

  ```python
  txt = "The rain in Spain"
  x = re.split("\s", txt, 2)
  print(x)
  ```

  

4. sub()

- 그것 대신 다른걸로 대체하고 싶을 때 쓴다

```python
txt = "The rain in Spain"
x = re.sub("\s", 9, txt)
print(x)

### 이를 두번 시행한다
txt = "The rain in Spain"
x = re.sub("\s", 9, txt, 2)
print(x)


```





```python
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
```

