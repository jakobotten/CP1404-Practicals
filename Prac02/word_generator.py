import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
all_letters = VOWELS + CONSONANTS
FORMAT_TYPES = "#%*"

print("Enter a word format")
print("\ttype % for a random consonant")
print("\ttype# for a random vowel")
print("\ttype* for a random letter")
print("\ttype random for a random word format")
print("\tall other letters will remain unchanged")

word_format = input("\t> ").lower()

format_length = random.randint(2,8)

if word_format == "random":
    word_format = ""
    for i in range(0, format_length):
        word_format += random.choice(FORMAT_TYPES)

word = ""

for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(all_letters)
    else:
        word += kind
print(word)
