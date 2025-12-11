import os 

# specify the directory path 
directory_path = '/'


# list all the files and directories  in the specified path
contents = os.listdir(directory_path)

# print each fle and directory name 

for item in contents:
    print(item)