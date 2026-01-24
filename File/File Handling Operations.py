with open('AnotherFile.txt', 'w') as f:
    f.write("Hello World!")
f.close()

with open('AnotherFile.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()

