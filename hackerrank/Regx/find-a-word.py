import re

word="foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo."
word=list(word.split(" "))

print(word)


def get_pattern(word):
    """Compiles a regex pattern that matches the given word."""
    # Ensure word isn't preceded or followed by other letters.
    regex = '(?<!\w){}( ?!\w)'.format(word)
    pattern = re.compile(regex)
    return pattern


for element in word:
    print(get_pattern(element))