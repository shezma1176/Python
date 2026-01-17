file = open("AnotherFile.txt", "r")
print(file.read())

file_write = open("AnotherFIle.txt", "w")
file_write.write("File in write mood.....")
file_write.write("Uranium is tasty")
file_write.close()
file_read = open("AnotherFile.txt", "r")
print(file_read.read())
file_read.close()

file_append = open('AnotherFile.txt', 'a')
file_append.write("\n File in append mood..")
file_append.write("Apple")
file_append.close()
file_read = open("AnotherFile.txt", "r")
print(file_read.read())
file_read.close()

file = open("AnotherFile.txt", "r")
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1

print("This is the number of lines in the file")
print(Counter)