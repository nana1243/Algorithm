

## 컴파일 옵션

정규식을 컴파일할 때 다음 옵션을 사용할 수 있다.

- DOTALL(S) - `.` 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
- IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
- MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (`^`, `$` 메타문자의 사용과 관계가 있는 옵션이다)
- VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)

옵션을 사용할 때는 `re.DOTALL`처럼 전체 옵션 이름을 써도 되고 `re.S`처럼 약어를 써도 된다.

### DOTALL, S

`.` 메타 문자는 줄바꿈 문자(`\n`)를 제외한 모든 문자와 매치되는 규칙이 있다. 만약 `\n` 문자도 포함하여 매치하고 싶다면 `re.DOTALL` 또는 `re.S` 옵션을 사용해 정규식을 컴파일하면 된다.

다음 예를 보자.

```python
>>> import re
>>> p = re.compile('a.b')
>>> m = p.match('a\nb')
>>> print(m)
None
```

정규식이 `a.b`인 경우 문자열 `a\nb`는 매치되지 않음을 알 수 있다. 왜냐하면 `\n`은 `.` 메타 문자와 매치되지 않기 때문이다. `\n` 문자와도 매치되게 하려면 다음과 같이 `re.DOTALL` 옵션을 사용해야 한다.

```python
>>> p = re.compile('a.b', re.DOTALL)
>>> m = p.match('a\nb')
>>> print(m)
<_sre.SRE_Match object at 0x01FCF3D8>
```

보통 `re.DOTALL` 옵션은 여러 줄로 이루어진 문자열에서 `\n`에 상관없이 검색할 때 많이 사용한다.







### IGNORECASE, I

`re.IGNORECASE` 또는 `re.I` 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션이다. 다음 예제를 보자.

```python
>>> p = re.compile('[a-z]', re.I)
>>> p.match('python')
<_sre.SRE_Match object at 0x01FCFA30>
>>> p.match('Python')
<_sre.SRE_Match object at 0x01FCFA68>
>>> p.match('PYTHON')
<_sre.SRE_Match object at 0x01FCF9F8>
```

`[a-z]` 정규식은 소문자만을 의미하지만 re.I 옵션으로 대소문자 구별 없이 매치된다.





### MULTILINE, M

`re.MULTILINE` 또는 `re.M` 옵션은 조금 후에 설명할 메타 문자인 `^`, `$`와 연관된 옵션이다. 이 메타 문자에 대해 간단히 설명하자면 `^`는 문자열의 처음을 의미하고, `$`는 문자열의 마지막을 의미한다. 예를 들어 정규식이 `^python`인 경우 문자열의 처음은 항상 python으로 시작해야 매치되고, 만약 정규식이 `python$`이라면 문자열의 마지막은 항상 python으로 끝나야 매치된다는 의미이다.

다음 예를 보자.

```python
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
```

정규식 `^python\s\w+`은 python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미이다. 검색할 문자열 data는 여러 줄로 이루어져 있다.

이 스크립트를 실행하면 다음과 같은 결과를 돌려준다.

```
['python one']
```