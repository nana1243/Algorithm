# matching-anything-but-new-line
input="123.456.abc.def"
regex_pattern = r"^...\....\....\....$"

import re
print(re.match(regex_pattern,input))



################################################
s="""
2
<p>hennie</p>
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
"""
p=r'<(\w+\s)(.*?)>'
# p=r'<(\w+)\s?(.*?)'

import re
tags = {}
print(re.findall(p,s))


for tag, p in re.findall(r'<(\w+)\s?(.*?)>', s):
    attr = set(a for a in re.findall(r'(\w+)=[\'\"]', p))
    if tag not in tags:
        tags[tag] = attr
    else:
        tags[tag] |= attr

for tag in sorted(tags.keys()):
    print(tag + ':' + ','.join(sorted(tags[tag])))