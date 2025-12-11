m1='pay attentioin to your study..\n'
m2='hello\n'
m3='new\'t line\n'
f=open('msg','w')
f.write(m1)
f.write(m2)
f.write(m3)
f.close()
f=open('msg','r')
data=f.read()
print(data)
f.close()