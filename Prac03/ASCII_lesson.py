
def main():
    lower = 48
    upper = 123

    user_input = get_number(lower, upper)
    print("{:>4} {:>4}".format(user_input, chr(user_input)))


def get_number(lower, upper):
    print("Enter a number ({}-{}):".format(lower, upper))
    valid_input = False
    while not valid_input:
        try:
            user_number = int(input(">>> "))
            while user_number <= lower or user_number >= upper:
                print("Please enter a valid number!")
                user_number = int(input(">>> "))
            valid_input = True
            return user_number
        except ValueError:
            print("Please enter a valid number!")

main()