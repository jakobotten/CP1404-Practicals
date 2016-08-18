

def main():
    user_name = get_name()
    letter_frequency = int(input("Enter letter frequency: "))
    print_name(user_name, letter_frequency)


def print_name(user_name, frequency_of_letters):
    for i in range(0, len(user_name), frequency_of_letters):
        print(user_name[i], end="")


def get_name():
    user_name = input("Enter name: ")
    user_name.replace(" ", "")
    while user_name == "":
        print("Name can't be blank")
        user_name = input("Enter name:")
    return user_name

main()
