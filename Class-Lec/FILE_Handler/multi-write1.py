# file=open('my_file2','w')
# lines_to_write=[
#     "this is first line.\n",
#     "this is second line.\n",
#     "this is third line.\n"
# ]
# file.writelines(lines_to_write)

# with open('my_file1.txt','r') as file:
#  content=file.read()
#  print(content)
#  print()

# f=open('sample.txt','r')
# print(f.tell())
# print(f.read(3))
# print(f.tell())
# print(f.seekable())
# f.seek(8)
# print(f.read())
# f.close()


with open('my_filex.txt','wb') as f:
    f.write(b"hello python!")
    

with open('my_filex.txt','rb') as f:
    f.seek(0,0)
    print(f"positon after seaking to begning:{f.tell()}")
    print(f"read from begning: {f.read(5)}")

    f.seek(3,1)
    print(f"positon after seaking 3 bytes from current:{f.tell()}")
    print(f"read from current position: {f.read(3)}")