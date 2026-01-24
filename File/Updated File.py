output_file = open('Updated file.txt', 'w')
input_file = open('Repeated.txt', 'r')

Lines_Seen_So_Far = set()
print("Eliminating Duplicate Lines...")
for line in input_file:
    if line not in Lines_Seen_So_Far:
        output_file.write(line)
        Lines_Seen_So_Far.add(line)

input_file.close()
output_file.close()