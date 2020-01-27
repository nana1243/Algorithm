### hackerrank : Regex 



1.Matching Specific String

> 어떤 특정 글자와 match 시키는 문제
>
> TASK:
>
> You have a test string . Your task is to match the string `hackerrank`. This is case sensitive.

```python
Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
```



#### 2. Matching Digits & Non-Digit Characters

> TASK
>
> **Task**
>
> You have a test string . Your task is to match the pattern xxXxxXxxxx
> Here x  denotes a digit character, and X denotes a non-digit character.

```python
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
```



#### 3. 

**Task**

You have a test string .
Your task is to write a regex that will match with following conditions:

-  must be of length: **`6`**
- First character: **`1`**, **`2`** or **`3`**
- Second character: **`1`**, **`2`** or **`0`**
- Third character: **`x`**, **`s`** or **`0`**
- Fourth character: **`3`**, **`0`** , **`A`** or **`a`**
- Fifth character: **`x`**, **`s`** or **`u`**
- Sixth character: **`.`** or **`,`**

```python
Regex_Pattern = r'^[1-3][0-2][x,s,0][3,0,A,a][x,s,u][.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
```







4. excluding

   **Task**

   You have a test string .
   Your task is to write a regex that will match with the following conditions:

   -  must be of length **`6`**.
   - First character should *not* be a **`digit`** ( or ).
   - Second character should *not* be a **`lowercase vowel`** ( or ).
   - Third character should *not* be **`b`**, **`c`**, **`D`** or **`F`**.
   - Fourth character should *not* be a **`whitespace character`** ( \r, \n, \t, \f or <space> ).
   - Fifth character should *not* be a **`uppercase vowel`** ( or ).
   - Sixth character should *not* be a **`.`** or **`,`** symbol.

   ```python
   Regex_Pattern = r'^[^0-9][^a,e,i,o,u][^b,c,D,F][^\s][^A,E,I,O,U][^.,]$'	# Do not delete 'r'.
   
   import re
   
   print(str(bool(re.search(Regex_Pattern, input()))).lower())
   ```

   

5. 양수의 패턴 이해하기

**Task**

Write a RegEx that will match a string satisfying the following conditions:

- The string's length is s>=5.
- The first character must be a lowercase English alphabetic character.
- The second character must be a *positive* digit. Note that we consider zero to be neither positive nor negative.
- The third character must *not* be a lowercase English alphabetic character.
- The fourth character must *not* be an uppercase English alphabetic character.
- The fifth character must be an uppercase English alphabetic character.

```python
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
```





