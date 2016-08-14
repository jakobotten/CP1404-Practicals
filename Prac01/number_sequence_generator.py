x_value = int(input("Enter the first value: "))
y_value = int(input("Enter the second value: "))

print(
    "(1) Show the even numbers from {0} to {1}\n(2) Show the odd numbers from {0} to {1}\n(3) Show the squares from {0} to {1}\n(4) Exit the program\n".format(
        x_value, y_value))
user_selection = input()

while user_selection != "4":
    if user_selection == "1":
        print("Even numbers from {} to {}:".format(x_value, y_value))
        for i in range(x_value, y_value + 1):
            even_odd_check = i % 2
            if even_odd_check == 0:
                print(i, end=" ")

    elif user_selection == "2":
        print("Odd numbers from {} to {}:".format(x_value, y_value))
        for i in range(x_value, y_value + 1):
            even_odd_check = i % 2
            if even_odd_check == 1:
                print(i, end=" ")

    elif user_selection == "3":
        print("Squares from {} to {}".format(x_value, y_value))
        for i in range(x_value, y_value + 1):
            print(i * i, end=" ")

    else:
        print("Sorry, {} is an invalid input")

    print(
        "\n(1) Show the even numbers from {0} to {1}\n(2) Show the odd numbers from {0} to {1}\n(3) Show the squares from {0} to {1}\n(4) Exit the program\n".format(
            x_value, y_value))
    user_selection = input()

print("Program Quit")
