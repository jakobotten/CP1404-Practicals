import random


def get_random_numbers():
    numbers = []
    for i in range(6):
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers += [number]
    return numbers


def main():
    number_of_quickpicks = int(input("How many quick picks? "))
    for quickpick in range(number_of_quickpicks):
        for random_number in get_random_numbers()[:-1]:
            print("{:3}".format(random_number), end=" ")
        print("{:3}".format(get_random_numbers()[-1]))


main()

