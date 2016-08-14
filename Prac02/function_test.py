import string


def count_letters(string_in):
    count = 0
    for char in string_in:
        if char.lower() in string.ascii_lowercase:
            count += 1
    return count


def get_number_in_text(text):
    number = ""
    for char in text.lower():
        if char in string.digits:
            number += char
    return number



user_input = input()

number_from_text = get_number_in_text(user_input)

print("This string contains the numbers {}.".format(number_from_text))
