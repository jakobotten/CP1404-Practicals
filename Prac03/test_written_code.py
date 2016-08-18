user_name = input("What is your name: ")
user_name.replace(" ","")
while user_name == "":
    print("Name can't be blank")
    user_name = input("What is your name:")
for i in range(0,len(user_name),2):
    print(user_name[i],end="")