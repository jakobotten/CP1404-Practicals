def main():
    user_string = input("Enter a sentence: ")
    word_tally = {}
    words = user_string.split()

    for word in words:
        if word in word_tally:
            word_tally[word] += 1
        else:
            word_tally[word] = 1

    display_word_tally(word_tally)


def display_word_tally(word_tally):
    list_of_words = []
    longest_word = 0
    for key in word_tally:
        list_of_words += [key]
        if len(key) >= longest_word:
            longest_word = len(key)
    list_of_words.sort()
    for word in list_of_words:
        print("{0:{1}} : {2}".format(word, longest_word, word_tally[word]))


main()
