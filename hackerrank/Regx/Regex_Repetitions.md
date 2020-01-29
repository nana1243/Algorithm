## Hackers Rank 정리

> 1. 구성
>    - Introduction
>    - Character Class
>    - Repetitions
>    - Grouping and Capturing
>    - Backreferences
>    - Assertions
>    - Applications

## 3. Repetitions

1. Matching {x} Repetitions

   **Task**

   You have a test string S.
   Your task is to write a regex that will match **S** using the following conditions:

   - S must be of length equal to **`45`**.
   - The first **40** characters should consist of **`letters`**(both lowercase and uppercase), or of **`even digits`**.
   - The last **5** characters should consist of **`odd digits`** or **`whitespace characters`**.

   ```python
   Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'	# Do not delete 'r'.
   ```

2. Matching {x, y} Repetitions

   **Task**

   You have a test string **S** .
   Your task is to write a regex that will match **S** using the following conditions:

   -  S should begin with  **1 or  2**`digits`**.
   - After that **S**, should have **3** or more **`letters`** (both lowercase and uppercase).
   - Then **S** should end with up to 3**`.`** symbol(s). You can end with to `.` symbol(s), inclusively.

```python
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}[.]{0,3}$'
```





3. Matching Zero Or More Repetitions

   

   **For Example**:

   **w\*** : It will match the character `w` or more times.
   **[xyz]\*** : It will match the characters `x`, `y` or `z` or more times.
   **\d\*** : It will match any digit or more times.

   ------

   **Task**

   You have a test string **S** .
   Your task is to write a regex that will match **S** using the following conditions:

   -  **s** should begin with **2** or more **`digits`**.
   - After that, **S** should have **0** or more **`lowercase letters`**.
   -  **S** should end with **0** or more **`uppercase letters`**

   ```python
   Regex_Pattern = r'^\d{2,}[a-z]{0,}[A-Z]{0,}$'	# Do not delete 'r'.
   ```

4.matching-one-or-more-repititions

**For Example**:

**w+** : It will match the character `w` or more times.
**[xyz]+** : It will match the character `x`, `y` or `z` or more times.
**\d+** : It will match any digit or more times.

------

**Task**

You have a test string **S**.
Your task is to write a regex that will match **S** using the following conditions:

-  **S** should begin **1** with or more **`digits`**.
- After that, **S** should have **1** or more **`uppercase letters`**.
-  **S** should end with **1** or more **`lowercase letters`**.

```python
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'	# Do not delete 'r'.
```





5. matching-ending-items

**Task**

Write a RegEx to match a test string, , under the following conditions:

-  **S** should consist of only lowercase and uppercase letters (no numbers or symbols).
-  **S** should end in `s`.

```python
Regex_Pattern = r'^[a-zA-Z]{0,}s{1}$'
```

