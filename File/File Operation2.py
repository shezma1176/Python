#Create New File

new_file = open('New File.txt', 'x')
new_file.close()

#Checking if file exists
import os
print("Checking if my_file exists or not...")
if os.path.exists('My File.txt'):
    os.remove('My File.txt')
else:
    print("The file does not exist") 

# Create a new if it doesnt
my_file = open('My_File.txt', 'w')
my_file.write("Hello I am Penguin!")
my_file.close()

# delete file
os.remove('Myself.txt')

# The most risky,dangerous code: os.rmdir('Folder')