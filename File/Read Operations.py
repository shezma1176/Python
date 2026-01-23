file = open('Read Operations.txt', 'r')
print(file.read())
file.close()

file = open('Read Operations.txt', 'r')
print("\n Read In Parts \n")
print(file.read(14))
file.close()

file = open('Read Operations.txt', 'r')

print(file.readline())
print(file.readline())
print(file.readline())

file.close()