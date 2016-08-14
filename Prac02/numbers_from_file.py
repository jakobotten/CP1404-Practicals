number_file = open("numbers.txt","r")
total = 0
for line in number_file:
    number = int(line)
    total += number
print(total)
number_file.close()
