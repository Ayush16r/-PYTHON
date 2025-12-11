# f=open("message","r+")
# print(f.read())
# f.write("writing in r+ mode")
# print(f.read())
# f.close()


f=open("message1","a")
f.write("writing in a mode")
# f.seek(0)
# print(f.read())
f.close()

f=open("message1","x")
f.write("writing in a mode")
# f.seek(0)
# print(f.read())
f.close()