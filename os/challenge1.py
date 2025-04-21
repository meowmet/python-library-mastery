# Challenge 1: Working with the os library

# Step 1: Create a directory named 'test_dir'
# Your code goes here to create the 'test_dir' folder

# Step 2: Create 3 text files inside 'test_dir'
# Your code goes here to create 'file1.txt', 'file2.txt', and 'file3.txt' inside 'test_dir'

# Step 3: List the files inside 'test_dir'
# Your code goes here to list the files in 'test_dir'

# Step 4: Delete the files and the directory
# Your code goes here to delete 'file1




import os
# import shutil

os.mkdir('test_dir')
for i in range(3):
    open(f"test_dir/file{i+1}.txt", 'w').close()


print(os.listdir("test_dir"))

# shutil.rmtree('test_dir') #thats just one line but need shutil lib

for file in os.listdir("test_dir"):
    os.remove(f"test_dir/{file}")

os.rmdir('test_dir')
