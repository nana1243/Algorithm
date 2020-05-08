## Hackers Rank 정리

> 1. 구성
>    - Introduction
>    - Character Class
>    - Repetitions
>    - Grouping and Capturing
>    - Backreferences
>    - Assertions
>    - Applications



## 7. Applications



### 1.find-a-word

We define a word as a non-empty maximum sequence of characters that can contain only lowercase letters, uppercase letters, digits and underscores '_' (ASCII value 95). Maximum sequence means that the word has to be immediately preceeded by a character not allowed to occur in a word or by the left boundary of the sentence, and it has to be immediately followed by a character not allowed to occur in a word or by the right boundary of the sentence.

Given sentences and words, for each of these words, find the number of its occurences in all the sentences.

**Input Format**

In the first line there is a single integer . Each of the next lines contains a single sentence. After that, in the next line, there is a single integer denoting the number of words. In the -th of the next lines, there is a single word denoting the -th word for which, you have to find the number of its occurences in the sentences.

**Constraints**



**Output format**

For every word, print the number of occurrences of the word in all the N sentences listed.

**Sample Input**

```
1
foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.
1
foo
```

**Sample Output**

```
6
```

**Explanation**

- foo is the first word
- (foo) is preceeded by '(' and followed by ')', so it's the second word.
- foo-bar is considered as two words and 'foo' is the first of them. It is preceeded by a space and followed by a hyphen '-'
- bar-foo also contains foo for the same reason mentioned above
- foo_bar is a single single word and hence foo in it is not counted
- foo'bar is considered as two words and 'foo' is the first of them. It is preceeded by a space and followed by a apostrophe "'"
- foo. as it is preceeded by a space and followed by a dot'.'

```python
import re


def count_occurrences(lines, words):
    
    for word in words:
        pattern = get_pattern(word)
        count = sum(len(pattern.findall(line)) for line in lines)
        print(count)


def get_pattern(word):
    regex = '(?<!\w){0}(?!\w)'.format(word)
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    line_count = int(input())
    lines = [input() for _ in range(line_count)]
    word_count = int(input())
    words = (input() for _ in range(word_count))
    count_occurrences(lines, words)

```





### 2. detect-the-email-addresses



#### 80 percentage 만 맞음 - 다시 체크

You will be provided with a block of text, spanning not more than hundred lines. Your task is to find the unique e-mail addresses present in the text. You could use Regular Expressions to simplify your task. And remember that the "@" sign can be used for a variety of purposes!

**Input Format**

The first line contains an integer N (N<=100), which is the number of lines present in the text fragment which follows.
From the second line, begins the text fragment (of N lines) in which you need to search for e-mail addresses.

**Output Format**

All the unique e-mail addresses detected by you, in one line, in lexicographical order, with a semi-colon as the delimiter.

**Sample Input**

```
19
HackerRank is more than just a company
    We are a tight group of hackers, bootstrappers, entrepreneurial thinkers and innovators. We are building an engaged community of problem solvers. Imagine the intelligence and value that a room would hold if it contained hackers/problem solvers from around the world? We're building this online.
Hypothesis: Every hacker loves a particular type of challenge presented in a certain set of difficulty. If we build a large collection of real world challenges in different domains with an engaging interface, it is going to be incredible! Join us to create history.
Available Positions
Product Hacker product@hackerrank.com
Challenge Curator
Product Evangelist
Product Designer
Content Creator
ACM World Finals Hacker
Backend C++ Hacker
Mail us at hackers@hackerrank.com to chat more. Or you can write to us at interviewstreet@hackerrank.com!
HACKERRANK PERKS
Working for a startup is hard work, but there are plenty of benefits of working for a small, fun, growing team.
[Image] Perk: Get tools for the jobAll the Right ToolsWe know that everyone's perfect workspace is unique to them. We will get you set up with whatever equipment you need to start hacking - a new 15” Macbook Pro or iMac, or a computer of your choice plus a display if you need it. Additionally, if you require any software or other tools, we've got it covered.[Image] Perk: Flexible HoursFlexible HoursBecause we work so hard, we encourage our employees to keep flexible hours and don't require them to track their time. A morning scrum and open communication ensures that the job gets done on time, and we rely on the honor system so that you can work on your own pace.[Image] Perk: HealthcareWellness SupportTo work hard, you have to be healthy. We will cover your health, dental, and visual insurance with no wait period. That means instant benefits from the day you're hired.[Image] Perk: Choice of LocationLocation, Location, LocationWe are the first Indian company to be backed by Y-Combinator, and as a result we have a thriving office in Bangalore and a growing office in Mountain View, CA. Depending on your residency or visa status, we will get you situated in one of our two offices, both of which are located in the heart of their country's tech industry.[Image] Perk: Choice of LocationCreative SupportIf you have a cool side project that you want to launch, we will pay for EC2/heroku servers to get it off the ground. Side projects fuel creativity and learning, which are crucial to the HackerRank culture.
CULTURE
The culture of a startup is reflective of the founders’ DNA. Larry Page & Sergey Brin were PhD’s from Stanford and that’s why Google is filled with high scoring graders from top schools and is very hard to get in if you’re not a CS major. Similarly, the hacker culture at Facebook is inspired by Zuckerberg, a hacker, the design culture by Steve Jobs and so on.
The adjective to describe the environment/founders here is relentless hardworkers. It might be a general trait of a startup but I’m pretty sure it’s a notch higher here and defines the culture. This is what has taken us this far. It’s not working in weekends or allnighters that count, but the effort that goes into building something intellectually engaging for hackers and making it fun is high.
You’ll have to embrace randomness and chaos. There’s some level of discipline (eg: daily scrums) but only so much. We push boundaries everyday, stretch our limits but no one complains because there’s a feeling of doing something great at the end of the day, every single day.
```

**Sample Output**

```
    hackers@hackerrank.com;interviewstreet@hackerrank.com;product@hackerrank.com
```



````python
# Enter your code here. Read input from STDIN. Print output to STDOUT

regex='([a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)'
import re
import sys

a=re.findall(regex, sys.stdin.read())
a=list(set(a))
a.sort()
sys.stdout.write(';'.join(item for item in a))

````

