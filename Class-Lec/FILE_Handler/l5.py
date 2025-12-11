import os
current_dir = os.getcwd()
print(f" current working directory: {current_dir}")
for item in os.listdir(current_dir):
    print(item)


new_dir_name= "my_new_dir"
if not os.path.exists(new_dir_name):
    os.mkdir(new_dir_name)
    print(f"directory '{new_dir_name}' created.")
else: 
    print(f"directory'{new_dir_name}' already created.")
print("infromation listdir(.)")
print(os.listdir('.'))
print("infromation listdir(..)")
print(os.listdir('..'))
print("files exist or not")
print(os.path.isdir("mydir"))
os.rmdir(new_dir_name)

os.chdir("CSW1_PYTHON_2025")
print(os.getcwd())


file_


else:
print(f"file")