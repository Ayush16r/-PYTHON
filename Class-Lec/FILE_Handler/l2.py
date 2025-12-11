# create a new file sample1.txt  
# we are learning  file io in the next line using java 
# i like prograaming in java 

# replace all ocurence of java with python
# search if the word learning exixts in the file or not




with open("sample1.txt", "r") as f:
    data = f.read()
data_r = data.replace("java", "python")
with open("sample1.txt", "w") as f:
    f.write(data_r)
if "learning" in data_r:
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does NOT exist in the file.")
print("\nUpdated File Content:\n")

