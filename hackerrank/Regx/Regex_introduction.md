## Hackers Rank 정리

> 1. 구성
>    - Introduction
>    - Character Class
>    - Repetitions
>    - Grouping and Capturing
>    - Backreferences
>    - Assertions
>    - Applications



### 1. INTRODUCTION



SOL1 Matching Specific String

**Task**

You have a test string . Your task is to match the string `hackerrank`. This is case sensitive.

```python
Regex_Pattern = "hackerrank"
```



SOL2 matching-anything-but-new-line

![matching-anything-but-new-line](https://user-images.githubusercontent.com/52269210/73343620-3fd26e00-42c4-11ea-86ff-0426a0231079.JPG)

```python
regex_pattern = '^.{3}\\..{3}\\..{3}\\..{3}$'
```

SQL3. matching-digits-non-digit-character

![matching-digits-non-digit-character](https://user-images.githubusercontent.com/52269210/73343621-3fd26e00-42c4-11ea-92a3-784298f2f1c0.JPG)

```python
Regex_Pattern = '\d\d\D\d\d\D\d\d\d\d'
```



SQL4. matching-whitespace-non-whitespace-character

![matching-whitespace-non-whitespace-character](https://user-images.githubusercontent.com/52269210/73343618-3f39d780-42c4-11ea-9b6d-70f6aa4699f6.JPG)

```python
Regex_Pattern = '\S\S\s\S\S\s\S\S'
```

SQL5. matching-word-non-word

![matching-word-non-word](https://user-images.githubusercontent.com/52269210/73343619-3f39d780-42c4-11ea-8787-c79e8185834f.JPG)

```python
Regex_Pattern = '\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w'
```

SQL6. matching-start-end

![matching-start-end](https://user-images.githubusercontent.com/52269210/73343617-3f39d780-42c4-11ea-815d-89a8414dc691.JPG)

```python
Regex_Pattern = '^\d\w\w\w\w\.$'
```

