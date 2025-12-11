import re
data="hello\nworld"
pattern=r'.'
matches=re.findall(pattern,data,re.DOTALL)
print(matches)

import re
data="hello.world"
pattern=r'\w+\.\w+ #pattern for data'
matches=re.findall(pattern,data,re.DOTALL)
print(matches)