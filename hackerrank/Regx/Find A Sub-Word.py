
if __name__ == '__main__':
    line_count = int(input())
    lines = [input() for _ in range(line_count)]
    word_count = int(input())
    words = (input() for _ in range(word_count))


# lines="existing pessimist optimist this is"
# words=["is","hi"]


import re
def get_pattern(word):
    regex = '([a-zA-Z]+{0}[a-zA-Z]+)'.format(word)
    pattern = re.compile(regex)
    return pattern

for w in words:
    p = get_pattern(w)
    print(len(re.findall(p, lines)))


