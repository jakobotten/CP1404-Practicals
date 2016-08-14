
user_name = input("Please enter your name: ")

name_file = open('name.txt', mode='w')

print(user_name, file=name_file)

name_file.close()
