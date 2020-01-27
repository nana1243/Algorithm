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





## 1.Metacharacters



| Character | Description                                                  | Example        | Try it                                                       |
| :-------- | :----------------------------------------------------------- | :------------- | :----------------------------------------------------------- |
| []        | A set of characters                                          | "[a-m]"        | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta1) |
| \         | Signals a special sequence (can also be used to escape special characters) | "\d"           | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta2) |
| .         | Any character (except newline character)                     | "he..o"        | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta3) |
| ^         | Starts with                                                  | "^hello"       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta4) |
| $         | Ends with                                                    | "world$"       | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta5) |
| *         | Zero or more occurrences                                     | "aix*"         | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta6) |
| +         | One or more occurrences                                      | "aix+"         | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta7) |
| {}        | Exactly the specified number of occurrences                  | "al{2}"        | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta8) |
| \|        | Either or                                                    | "falls\|stays" | [Try it »](https://www.w3schools.com/python/showpython.asp?filename=demo_regex_meta9) |
| ()        | Capture and group                                            |                |                                                              |



1-1  "." :Any character (except newline character)

```python
txt="hello i am java"
x=re.compile("he..o",txt)
print(x)
>>['hello']
```



1-2  ^hello : start with hello

```python
import re

txt = "hello world"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
>>['hello']


txt = "i am java hello world"
x = re.findall("^hello", txt)
>>[] # 빈집합이 나온다



```



cf> startwith 함수 

```python
for i in list(txt.split(" ")):
    print(i.startswith("hello"))
####### 값이 true or false 값이 나온다 ######
```



1-3 * :  

> go*gle 이라는 정규식을 보겠습니다.
>
> 여기서 반복의 의미를 가진 메타문자 * 는 해당 메타문자 앞의 문자가 0번이상 무한대로 반복될 수 있음을 의미합니다.
>
> 즉, go*gle 이라는 정규식은, "ggle", "gogle", "google", "goooooooogle" 과 모두 매치됩니다.

1-4 + 

> **네번째, 반복(+)**
>
> 반복을 나타내는 메타문자는 하나 더 있습니다. 바로 + 인데 *와 다른 점은, + 메타문자는 반복 회수가 최소 1번이상이어야 합니다.
>
> 즉, go+gle 이라는 정규식에 대해 "ggle"은 매치되지 않습니다

 



1-5 {m} or {m,n}

**1.** {m}

```
ca{2}t
```

위 정규식의 의미는 다음과 같다.

> "c + a(반드시 2번 반복) + t"

위 정규식에 대한 매치여부는 다음 표와 같다.

| 정규식   | 문자열 | Match 여부 | 설명                               |
| :------- | :----- | :--------- | :--------------------------------- |
| `ca{2}t` | cat    | No         | "a"가 1번만 반복되어 매치되지 않음 |
| `ca{2}t` | caat   | Yes        | "a"가 2번 반복되어 매치            |

**2.** {m, n}

```
ca{2,5}t
```

위 정규식의 의미는 다음과 같다:

> "c + a(2~5회 반복) + t"

위 정규식에 대한 매치여부는 다음 표와 같다.

| 정규식     | 문자열  | Match 여부 | 설명                               |
| :--------- | :------ | :--------- | :--------------------------------- |
| `ca{2,5}t` | cat     | No         | "a"가 1번만 반복되어 매치되지 않음 |
| `ca{2,5}t` | caat    | Yes        | "a"가 2번 반복되어 매치            |
| `ca{2,5}t` | caaaaat | Yes        | "a"가 5번 반복되어 매치            |



#### 3.** `?`

반복은 아니지만 이와 비슷한 개념으로 `?` 이 있다. `?` 메타문자가 의미하는 것은 `{0, 1}` 이다.

다음 정규식을 보자.

```
ab?c
```

위 정규식의 의미는 다음과 같다:

> "a + b(있어도 되고 없어도 된다) + c"

위 정규식에 대한 매치여부는 다음 표와 같다.

| 정규식 | 문자열 | Match 여부 | 설명                    |
| :----- | :----- | :--------- | :---------------------- |
| `ab?c` | abc    | Yes        | "b"가 1번 사용되어 매치 |
| `ab?c` | ac     | Yes        | "b"가 0번 사용되어 매치 |



