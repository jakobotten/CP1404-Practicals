user_name = input("Enter name: ")

print(
    """
(H)ello
(G)oodbye
(Q)uit
    """)
user_selection = input()

while user_selection != "Q":
    if user_selection == "H":
        print("Hello {}".format(user_name))
    elif user_selection == "G":
        print("Goodbye {}".format(user_name))
    else:
        print("Invalid input, please try again.")
    print(
        """
(H)ello
(G)oodbye
(Q)uit
        """)
    user_selection = input()

print("Finished")
