import re

text='alias'
pattern='^a...s$'
result=re.match(pattern,text)
if result:
    print('matching')
else:
    print('not matching')