import re
data='''abc 123
xyz 456
mnp 789'''
pattern=r'\d{3}$'
matches=re.findall(pattern,data)

#re.MULTILINE or re.M
import re
data='''abc 123
xyz 456
mnp 789'''
pattern=r'\d{3}$'
matches=re.findall(pattern,data,re.MULTILINE)
print(matches)