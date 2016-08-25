def print_things(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    mean_value = sum(numbers) / len(numbers)
    print("The average of the numbers is {}".format(mean_value))


def main():
    numbers = []
    for i in range(0, 5):
        numbers += [int(input("Number: "))]
    print_things(numbers)


main()

