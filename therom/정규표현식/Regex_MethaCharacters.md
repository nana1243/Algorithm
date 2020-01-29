## 1.Metacharacters



|  원래 표현식   | 축약 표현 | 부연 설명                                                    | 사용처                             |
| :------------: | :-------: | :----------------------------------------------------------- | :--------------------------------- |
|     [0-9]      |    \d     | 숫자를 찾는다                                                | 숫자                               |
|     [^0-9]     |    \D     | 숫자가 아닌 것을 찾는다                                      | 텍스트 + 특수문자 + 화이트스페이스 |
| [ \t\n\r\f\v]  |    \s     | whitespace 문자인 것을 찾는다                                | 스페이스, TAB, 개행(new line)      |
| [^ \t\n\r\f\v] |    \S     | whitespace 문자가 아닌 것을 찾는다                           | 텍스트 + 특수문자 + 숫자           |
|  [a-zA-Z0-9]   |    \w     | 문자+숫자인 것을 찾는다. (특수문자는 제외. 단, 언더스코어 포함) | 텍스트 + 숫자                      |
|  [^a-zA-Z0-9]  |    \W     | 문자+숫자가 아닌 것을 찾는다.                                | 특수문자 + 공백                    |

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



### 1-1  "." :Any character (except newline character)

```python
txt="hello i am java"
x=re.compile("he..o",txt)
print(x)
>>['hello']
```



### 1-2  ^hello : start with hello

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

### 1-3. *

  

> go*gle 이라는 정규식을 보겠습니다.
>
> 여기서 반복의 의미를 가진 메타문자 * 는 해당 메타문자 앞의 문자가 0번이상 무한대로 반복될 수 있음을 의미합니다.
>
> 즉, go*gle 이라는 정규식은, "ggle", "gogle", "google", "goooooooogle" 과 모두 매치됩니다.

### 1-4. +

> **네번째, 반복(+)**
>
> 반복을 나타내는 메타문자는 하나 더 있습니다. 바로 + 인데 *와 다른 점은, + 메타문자는 반복 회수가 최소 1번이상이어야 합니다.
>
> 즉, go+gle 이라는 정규식에 대해 "ggle"은 매치되지 않습니다

 



### 1-5 {m} or {m,n}

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



#### 1-6. `?`

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







### 1.7 ' | '

`|` 메타 문자는 or과 동일한 의미로 사용된다. `A|B`라는 정규식이 있다면 A 또는 B라는 의미가 된다.

```python
>>> p = re.compile('Crow|Servo')
>>> m = p.match('CrowHello')
>>> print(m)
<re.Match object; span=(0, 4), match='Crow'>
```





### 1-8. $

`$` 메타 문자는 `^` 메타 문자와 반대의 경우이다. 즉 `$`는 문자열의 끝과 매치함을 의미한다.

다음 예를 보자.

```python
>>> print(re.search('short$', 'Life is too short'))
<re.Match object; span=(12, 17), match='short'>
>>> print(re.search('short$', 'Life is too short, you need python'))
None
```



`short$` 정규식은 검색할 문자열이 short로 끝난 경우에는 매치되지만 그 이외의 경우에는 매치되지 않음을 알 수 있다.

> ※ `^` 또는 `$` 문자를 메타 문자가 아닌 문자 그 자체로 매치하고 싶은 경우에는 `\^`, `\$` 로 사용하면 된다.





