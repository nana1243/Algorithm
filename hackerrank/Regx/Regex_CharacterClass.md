## Hackers Rank 정리

> 1. 구성
>    - Introduction
>    - Character Class
>    - Repetitions
>    - Grouping and Capturing
>    - Backreferences
>    - Assertions
>    - Applications

## 2. Character Class



SOL1.matching-specific-characters

![matching-specific](https://user-images.githubusercontent.com/52269210/73344569-ec611f80-42c5-11ea-98ba-ca35711fa378.JPG)

```python
Regex_Pattern = '^[123][120][xs0][30Aa][xsu][.,]$'
```



SOL2. excluding-specific-characters

![excluding-specific-characters](https://user-images.githubusercontent.com/52269210/73344567-ebc88900-42c5-11ea-911f-88f4b8db25e9.JPG)

```python
Regex_Pattern = '^[^\d][^aeiou][^bcDF]\S[^AEIOU][^.,]$'
```



SOL3. matching-range-of-characters

![matching-range-of-characters](https://user-images.githubusercontent.com/52269210/73344568-ebc88900-42c5-11ea-9cb4-49154248d05f.JPG)

```python
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
```

